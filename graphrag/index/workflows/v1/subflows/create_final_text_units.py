# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""All the steps to transform the text units."""

from typing import cast

import pandas as pd
from datashaper import (
    Table,
    VerbCallbacks,
    VerbInput,
    VerbResult,
    create_verb_result,
    verb,
)

from graphrag.index.cache import PipelineCache
from graphrag.index.flows.create_final_text_units import (
    create_final_text_units as create_final_text_units_flow,
)
from graphrag.index.utils.ds_util import get_named_input_table, get_required_input_table


@verb(name="create_final_text_units", treats_input_tables_as_immutable=True)
async def create_final_text_units(
    input: VerbInput,
    callbacks: VerbCallbacks,
    cache: PipelineCache,
    text_embed: dict | None = None,
    **_kwargs: dict,
) -> VerbResult:
    """All the steps to transform the text units."""
    source = cast(pd.DataFrame, input.get_input())
    final_entities = cast(
        pd.DataFrame, get_required_input_table(input, "entities").table
    )
    final_relationships = cast(
        pd.DataFrame, get_required_input_table(input, "relationships").table
    )
    final_covariates = get_named_input_table(input, "covariates")

    if final_covariates:
        final_covariates = cast(pd.DataFrame, final_covariates.table)

    output = await create_final_text_units_flow(
        source,
        final_entities,
        final_relationships,
        final_covariates,
        callbacks,
        cache,
        text_embed,
    )

    return create_verb_result(cast(Table, output))
