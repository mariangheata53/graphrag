# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Common default configuration values."""

from pathlib import Path

from graphrag.config.enums import (
    AsyncType,
    AuthType,
    CacheType,
    ChunkStrategyType,
    InputFileType,
    InputType,
    LLMType,
    NounPhraseExtractorType,
    OutputType,
    ReportingType,
    TextEmbeddingTarget,
)
from graphrag.vector_stores.factory import VectorStoreType

DEFAULT_CHAT_MODEL_ID = "default_chat_model"
DEFAULT_EMBEDDING_MODEL_ID = "default_embedding_model"
ASYNC_MODE = AsyncType.Threaded
ENCODING_MODEL = "cl100k_base"
AZURE_AUDIENCE = "https://cognitiveservices.azure.com/.default"
AUTH_TYPE = AuthType.APIKey
#
# LLM Parameters
#
LLM_FREQUENCY_PENALTY = 0.0
LLM_TYPE = LLMType.OpenAIChat
LLM_MODEL = "gpt-4-turbo-preview"
LLM_MAX_TOKENS = 4000
LLM_TEMPERATURE = 0
LLM_TOP_P = 1
LLM_N = 1
LLM_REQUEST_TIMEOUT = 180.0
LLM_TOKENS_PER_MINUTE = 50_000
LLM_REQUESTS_PER_MINUTE = 1_000
LLM_MAX_RETRIES = 10
LLM_MAX_RETRY_WAIT = 10.0
LLM_PRESENCE_PENALTY = 0.0
LLM_SLEEP_ON_RATE_LIMIT_RECOMMENDATION = True
LLM_CONCURRENT_REQUESTS = 25

PARALLELIZATION_STAGGER = 0.3
PARALLELIZATION_NUM_THREADS = 50

#
# Text embedding
#
EMBEDDING_TYPE = LLMType.OpenAIEmbedding
EMBEDDING_MODEL = "text-embedding-3-small"
EMBEDDING_BATCH_SIZE = 16
EMBEDDING_BATCH_MAX_TOKENS = 8191
EMBEDDING_TARGET = TextEmbeddingTarget.required
EMBEDDING_MODEL_ID = DEFAULT_EMBEDDING_MODEL_ID

# LLM response caching
CACHE_TYPE = CacheType.file
CACHE_BASE_DIR = "cache"

# Text chunking
CHUNK_SIZE = 1200
CHUNK_OVERLAP = 100
CHUNK_GROUP_BY_COLUMNS = ["id"]
CHUNK_STRATEGY = ChunkStrategyType.tokens

# Claim extraction
DESCRIPTION = "Any claims or facts that could be relevant to information discovery."
CLAIM_MAX_GLEANINGS = 1
EXTRACT_CLAIMS_ENABLED = False
EXTRACT_CLAIMS_MODEL_ID = DEFAULT_CHAT_MODEL_ID

# Graph clustering
MAX_CLUSTER_SIZE = 10
USE_LCC = True
CLUSTER_GRAPH_SEED = 0xDEADBEEF

# Community report summarization
COMMUNITY_REPORT_MAX_LENGTH = 2000
COMMUNITY_REPORT_MAX_INPUT_LENGTH = 8000
COMMUNITY_REPORT_MODEL_ID = DEFAULT_CHAT_MODEL_ID

# Graph extraction via LLM
EXTRACT_GRAPH_ENTITY_TYPES = ["organization", "person", "geo", "event"]
EXTRACT_GRAPH_MAX_GLEANINGS = 1
EXTRACT_GRAPH_MODEL_ID = DEFAULT_CHAT_MODEL_ID

# Graph extraction via NLP
NLP_NORMALIZE_EDGE_WEIGHTS = True
NLP_EXTRACTOR_TYPE = NounPhraseExtractorType.RegexEnglish
NLP_MAX_WORD_LENGTH = 15
NLP_MODEL_NAME = "en_core_web_md"
NLP_EXCLUDE_NOUNS = None
NLP_WORD_DELIMITER = " "
NLP_INCLUDE_NAMED_ENTITIES = True
NLP_EXCLUDE_ENTITY_TAGS = ["DATE"]
NLP_EXCLUDE_POS_TAGS = ["DET", "PRON", "INTJ", "X"]
NLP_NOUN_PHRASE_TAGS = ["PROPN", "NOUNS"]
NLP_NOUN_PHRASE_CFG = {
    "PROPN,PROPN": "PROPN",
    "NOUN,NOUN": "NOUNS",
    "NOUNS,NOUN": "NOUNS",
    "ADJ,ADJ": "ADJ",
    "ADJ,NOUN": "NOUNS",
}

# Input file params
INPUT_FILE_TYPE = InputFileType.text
INPUT_TYPE = InputType.file
INPUT_BASE_DIR = "input"
INPUT_FILE_ENCODING = "utf-8"
INPUT_TEXT_COLUMN = "text"
INPUT_CSV_PATTERN = ".*\\.csv$"
INPUT_TEXT_PATTERN = ".*\\.txt$"

NODE2VEC_ENABLED = False
NODE2VEC_DIMENSIONS = 1536
NODE2VEC_NUM_WALKS = 10
NODE2VEC_WALK_LENGTH = 40
NODE2VEC_WINDOW_SIZE = 2
NODE2VEC_ITERATIONS = 3
NODE2VEC_RANDOM_SEED = 597832
REPORTING_TYPE = ReportingType.file
REPORTING_BASE_DIR = "logs"
SNAPSHOTS_GRAPHML = False
SNAPSHOTS_EMBEDDINGS = False
OUTPUT_BASE_DIR = "output"
OUTPUT_DEFAULT_ID = "default_output"
OUTPUT_TYPE = OutputType.file
SUMMARIZE_DESCRIPTIONS_MAX_LENGTH = 500
SUMMARIZE_MODEL_ID = DEFAULT_CHAT_MODEL_ID
UMAP_ENABLED = False
UPDATE_OUTPUT_BASE_DIR = "update_output"

# Graph Pruning
PRUNE_MIN_NODE_FREQ = 2
PRUNE_MAX_NODE_FREQ_STD = None
PRUNE_MIN_NODE_DEGREE = 1
PRUNE_MAX_NODE_DEGREE_STD = None
PRUNE_MIN_EDGE_WEIGHT_PCT = 40
PRUNE_REMOVE_EGO_NODES = False
PRUNE_LCC_ONLY = False

VECTOR_STORE_TYPE = VectorStoreType.LanceDB.value
VECTOR_STORE_DB_URI = str(Path(OUTPUT_BASE_DIR) / "lancedb")
VECTOR_STORE_CONTAINER_NAME = "default"
VECTOR_STORE_OVERWRITE = True
VECTOR_STORE_DEFAULT_ID = "default_vector_store"

# Local Search
LOCAL_SEARCH_TEXT_UNIT_PROP = 0.5
LOCAL_SEARCH_COMMUNITY_PROP = 0.15
LOCAL_SEARCH_CONVERSATION_HISTORY_MAX_TURNS = 5
LOCAL_SEARCH_TOP_K_MAPPED_ENTITIES = 10
LOCAL_SEARCH_TOP_K_RELATIONSHIPS = 10
LOCAL_SEARCH_MAX_TOKENS = 12_000
LOCAL_SEARCH_LLM_TEMPERATURE = 0
LOCAL_SEARCH_LLM_TOP_P = 1
LOCAL_SEARCH_LLM_N = 1
LOCAL_SEARCH_LLM_MAX_TOKENS = 2000

# Global Search
GLOBAL_SEARCH_LLM_TEMPERATURE = 0
GLOBAL_SEARCH_LLM_TOP_P = 1
GLOBAL_SEARCH_LLM_N = 1
GLOBAL_SEARCH_MAX_TOKENS = 12_000
GLOBAL_SEARCH_DATA_MAX_TOKENS = 12_000
GLOBAL_SEARCH_MAP_MAX_TOKENS = 1000
GLOBAL_SEARCH_REDUCE_MAX_TOKENS = 2_000
GLOBAL_SEARCH_CONCURRENCY = 32

# Global Search with dynamic community selection
DYNAMIC_SEARCH_LLM_MODEL = "gpt-4o-mini"
DYNAMIC_SEARCH_RATE_THRESHOLD = 1
DYNAMIC_SEARCH_KEEP_PARENT = False
DYNAMIC_SEARCH_NUM_REPEATS = 1
DYNAMIC_SEARCH_USE_SUMMARY = False
DYNAMIC_SEARCH_CONCURRENT_COROUTINES = 16
DYNAMIC_SEARCH_MAX_LEVEL = 2

# DRIFT Search
DRIFT_SEARCH_LLM_TEMPERATURE = 0
DRIFT_SEARCH_LLM_TOP_P = 1
DRIFT_SEARCH_LLM_N = 1
DRIFT_SEARCH_MAX_TOKENS = 12_000
DRIFT_SEARCH_DATA_MAX_TOKENS = 12_000
DRIFT_SEARCH_CONCURRENCY = 32

DRIFT_SEARCH_K_FOLLOW_UPS = 20
DRIFT_SEARCH_PRIMER_FOLDS = 5
DRIFT_SEARCH_PRIMER_MAX_TOKENS = 12_000

DRIFT_SEARCH_REDUCE_LLM_TEMPERATURE = 0
DRIFT_SEARCH_REDUCE_MAX_TOKENS = 2_000

DRIFT_LOCAL_SEARCH_TEXT_UNIT_PROP = 0.9
DRIFT_LOCAL_SEARCH_COMMUNITY_PROP = 0.1
DRIFT_LOCAL_SEARCH_TOP_K_MAPPED_ENTITIES = 10
DRIFT_LOCAL_SEARCH_TOP_K_RELATIONSHIPS = 10
DRIFT_LOCAL_SEARCH_MAX_TOKENS = 12_000
DRIFT_LOCAL_SEARCH_LLM_TEMPERATURE = 0
DRIFT_LOCAL_SEARCH_LLM_TOP_P = 1
DRIFT_LOCAL_SEARCH_LLM_N = 1
DRIFT_LOCAL_SEARCH_LLM_MAX_TOKENS = 2000

DRIFT_N_DEPTH = 3

# Basic Search
BASIC_SEARCH_TEXT_UNIT_PROP = 0.5
BASIC_SEARCH_CONVERSATION_HISTORY_MAX_TURNS = 5
BASIC_SEARCH_MAX_TOKENS = 12_000
BASIC_SEARCH_LLM_TEMPERATURE = 0
BASIC_SEARCH_LLM_TOP_P = 1
BASIC_SEARCH_LLM_N = 1
BASIC_SEARCH_LLM_MAX_TOKENS = 2000
