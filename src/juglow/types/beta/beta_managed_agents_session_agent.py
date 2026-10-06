# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .beta_managed_agents_custom_tool import BetaManagedAgentsCustomTool
from .beta_managed_agents_mcp_toolset import BetaManagedAgentsMCPToolset
from .beta_managed_agents_custom_track import BetaManagedAgentsCustomTrack
from .beta_managed_agents_model_config import BetaManagedAgentsModelConfig
from .beta_managed_agents_juglow_track import BetaManagedAgentsJuglowTrack
from .beta_managed_agents_agent_toolset20260401 import BetaManagedAgentsAgentToolset20260401
from .beta_managed_agents_mcp_server_url_definition import BetaManagedAgentsMCPServerURLDefinition
from .beta_managed_agents_session_multiagent_coordinator import BetaManagedAgentsSessionMultiagentCoordinator

__all__ = ["BetaManagedAgentsSessionAgent", "Track", "Tool"]

Track: TypeAlias = Annotated[
    Union[BetaManagedAgentsJuglowTrack, BetaManagedAgentsCustomTrack], PropertyInfo(discriminator="type")
]

Tool: TypeAlias = Annotated[
    Union[BetaManagedAgentsAgentToolset20260401, BetaManagedAgentsMCPToolset, BetaManagedAgentsCustomTool],
    PropertyInfo(discriminator="type"),
]


class BetaManagedAgentsSessionAgent(BaseModel):
    """Resolved `agent` definition for a `session`.

    Snapshot of the `agent` at `session` creation time.
    """

    id: str

    description: Optional[str] = None

    mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]

    model: BetaManagedAgentsModelConfig
    """Model identifier and configuration."""

    multiagent: Optional[BetaManagedAgentsSessionMultiagentCoordinator] = None
    """
    Resolved coordinator topology with full agent definitions for each roster
    member.
    """

    name: str

    tracks: List[Track]

    system: Optional[str] = None

    tools: List[Tool]

    type: Literal["agent"]

    version: int
