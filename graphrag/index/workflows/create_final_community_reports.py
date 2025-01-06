# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""A module containing run_workflow method definition."""

import pandas as pd

from graphrag.callbacks.workflow_callbacks import WorkflowCallbacks
from graphrag.config.models.graph_rag_config import GraphRagConfig
from graphrag.index.context import PipelineRunContext
from graphrag.index.flows.create_final_community_reports import (
    create_final_community_reports,
)
from graphrag.utils.storage import load_table_from_storage, write_table_to_storage

workflow_name = "create_final_community_reports"


async def run_workflow(
    config: GraphRagConfig,
    context: PipelineRunContext,
    callbacks: WorkflowCallbacks,
) -> pd.DataFrame | None:
    """All the steps to transform community reports."""
    nodes = await load_table_from_storage("create_final_nodes", context.storage)
    edges = await load_table_from_storage("create_final_relationships", context.storage)
    entities = await load_table_from_storage("create_final_entities", context.storage)
    communities = await load_table_from_storage(
        "create_final_communities", context.storage
    )
    claims = None
    if config.claim_extraction.enabled:
        claims = await load_table_from_storage(
            "create_final_covariates", context.storage
        )
    async_mode = config.community_reports.async_mode
    num_threads = config.community_reports.parallelization.num_threads
    summarization_strategy = config.community_reports.resolved_strategy(config.root_dir)

    output = await create_final_community_reports(
        nodes,
        edges,
        entities,
        communities,
        claims,
        callbacks,
        context.cache,
        summarization_strategy,
        async_mode=async_mode,
        num_threads=num_threads,
    )

    await write_table_to_storage(output, workflow_name, context.storage)

    return output
