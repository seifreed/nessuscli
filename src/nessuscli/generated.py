"""Generated typed wrappers for the Nessus API. Do not edit manually."""

from __future__ import annotations

import builtins
from pathlib import Path
from typing import Any

from .client import NessusClient
from .types import JsonValue, ResponseValue


class _TypedResource:
    """Base for generated resource facades."""

    def __init__(self, client: NessusClient) -> None:
        self._client = client


class AgentGroupsAPI(_TypedResource):
    """Typed operations for the agent-groups resource."""

    def add_agent(self, *, group_id: int, agent_id: int) -> ResponseValue:
        """Add an agent to the given agent group."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["group_id"] = group_id
        path["agent_id"] = agent_id
        return self._client.call(
            "agent-groups",
            "add-agent",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def add_agents(
        self, *, group_id: int, ids: builtins.list[JsonValue]
    ) -> ResponseValue:
        """Add multiple agents to the given agent group."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["group_id"] = group_id
        payload["ids"] = ids
        return self._client.call(
            "agent-groups",
            "add-agents",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def configure(self, *, group_id: int, name: str) -> ResponseValue:
        """Changes the name of the given agent group."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["group_id"] = group_id
        payload["name"] = name
        return self._client.call(
            "agent-groups",
            "configure",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def create(self, *, name: str) -> ResponseValue:
        """Create an agent group."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        payload["name"] = name
        return self._client.call(
            "agent-groups",
            "create",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def delete_group(self, *, group_id: int) -> ResponseValue:
        """Delete an agent group."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["group_id"] = group_id
        return self._client.call(
            "agent-groups",
            "delete-group",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def delete_groups(self, *, ids: builtins.list[JsonValue]) -> ResponseValue:
        """Delete multiple agent groups."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        payload["ids"] = ids
        return self._client.call(
            "agent-groups",
            "delete-groups",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def delete_agent(self, *, group_id: int, agent_id: int) -> ResponseValue:
        """Delete an agent from the given agent group."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["group_id"] = group_id
        path["agent_id"] = agent_id
        return self._client.call(
            "agent-groups",
            "delete-agent",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def delete_agents(
        self, *, group_id: int, ids: builtins.list[JsonValue]
    ) -> ResponseValue:
        """Delete multiple agents from the given agent group."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["group_id"] = group_id
        payload["ids"] = ids
        return self._client.call(
            "agent-groups",
            "delete-agents",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def details(self, *, group_id: int) -> ResponseValue:
        """Return details for the given agent group."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["group_id"] = group_id
        return self._client.call(
            "agent-groups",
            "details",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def list(self) -> ResponseValue:
        """Returns a list of agent groups."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "agent-groups",
            "list",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )


class AgentsAPI(_TypedResource):
    """Typed operations for the agents resource."""

    def delete(self, *, agent_id: int) -> ResponseValue:
        """Delete an agent."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["agent_id"] = agent_id
        return self._client.call(
            "agents",
            "delete",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def delete_bulk(self, *, ids: builtins.list[JsonValue]) -> ResponseValue:
        """Delete agents in bulk."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        payload["ids"] = ids
        return self._client.call(
            "agents",
            "delete-bulk",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def unlink(self, *, agent_id: int) -> ResponseValue:
        """
        Unlink an agent. Only works if the Track Unlinked Agents feature is enabled.
        """
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["agent_id"] = agent_id
        return self._client.call(
            "agents",
            "unlink",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def unlink_bulk(self, *, ids: builtins.list[JsonValue]) -> ResponseValue:
        """
        Unlink agents in bulk. Only works if the Track Unlinked Agents feature is
        enabled.
        """
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        payload["ids"] = ids
        return self._client.call(
            "agents",
            "unlink-bulk",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def list(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        filter_search_type: str | None = None,
        filter_filter_number_filter: str | None = None,
        filter_filter_number_quality: str | None = None,
        filter_filter_number_value: str | None = None,
    ) -> ResponseValue:
        """
        Returns the full list of agents unless a 'limit' parameter is specified.
        """
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        if limit is not None:
            query["limit"] = limit
        if offset is not None:
            query["offset"] = offset
        if sort_by is not None:
            query["sort_by"] = sort_by
        if sort_order is not None:
            query["sort_order"] = sort_order
        if filter_search_type is not None:
            query["filter.search_type"] = filter_search_type
        if filter_filter_number_filter is not None:
            query["filter.FILTER_NUMBER.filter"] = filter_filter_number_filter
        if filter_filter_number_quality is not None:
            query["filter.FILTER_NUMBER.quality"] = filter_filter_number_quality
        if filter_filter_number_value is not None:
            query["filter.FILTER_NUMBER.value"] = filter_filter_number_value
        return self._client.call(
            "agents",
            "list",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def list_one(self, *, agent_id: int) -> ResponseValue:
        """List an agent."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["agent_id"] = agent_id
        return self._client.call(
            "agents",
            "list-one",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )


class EditorAPI(_TypedResource):
    """Typed operations for the editor resource."""

    def audits(
        self,
        *,
        type: str,
        object_id: int,
        file_id: int,
        output_path: str | Path | None = None,
    ) -> ResponseValue:
        """Export the given audit file."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["type"] = type
        path["object_id"] = object_id
        path["file_id"] = file_id
        return self._client.call(
            "editor",
            "audits",
            path=path or None,
            query=query or None,
            payload=payload or None,
            output_path=output_path,
        )

    def audits_token_download(
        self, *, type: str, object_id: int, file_id: int
    ) -> ResponseValue:
        """
        Export the given audit file for download using a single use token.
        """
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["type"] = type
        path["object_id"] = object_id
        path["file_id"] = file_id
        return self._client.call(
            "editor",
            "audits-token-download",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def details(self, *, type: str, template_uuid: str) -> ResponseValue:
        """Returns details for the given template."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["type"] = type
        path["template_uuid"] = template_uuid
        return self._client.call(
            "editor",
            "details",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def edit(self, *, type: str, id: int) -> ResponseValue:
        """Returns the requested object."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["type"] = type
        path["id"] = id
        return self._client.call(
            "editor",
            "edit",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def list(self, *, type: str) -> ResponseValue:
        """Returns the template list."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["type"] = type
        return self._client.call(
            "editor",
            "list",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def plugin_description(
        self, *, policy_id: int, family_id: int, plugin_id: int
    ) -> ResponseValue:
        """Returns the plugin description"""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["policy_id"] = policy_id
        path["family_id"] = family_id
        path["plugin_id"] = plugin_id
        return self._client.call(
            "editor",
            "plugin-description",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )


class FileAPI(_TypedResource):
    """Typed operations for the file resource."""

    def upload(
        self, *, no_enc: int | None = None, file_path: str | Path
    ) -> ResponseValue:
        """Uploads a file."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        if no_enc is not None:
            payload["no_enc"] = no_enc
        return self._client.call(
            "file",
            "upload",
            path=path or None,
            query=query or None,
            payload=payload or None,
            file_path=file_path,
        )


class FoldersAPI(_TypedResource):
    """Typed operations for the folders resource."""

    def create(self, *, name: str) -> ResponseValue:
        """Create a new folder for the current user."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        payload["name"] = name
        return self._client.call(
            "folders",
            "create",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def delete(self, *, folder_id: int) -> ResponseValue:
        """Delete a folder."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["folder_id"] = folder_id
        return self._client.call(
            "folders",
            "delete",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def edit(self, *, folder_id: int, name: str) -> ResponseValue:
        """Rename a folder for the current user."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["folder_id"] = folder_id
        payload["name"] = name
        return self._client.call(
            "folders",
            "edit",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def list(self) -> ResponseValue:
        """Returns the current user's scan folders."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "folders",
            "list",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )


class GroupsAPI(_TypedResource):
    """Typed operations for the groups resource."""

    def add_user(self, *, group_id: int, user_id: int) -> ResponseValue:
        """Add a user to the group."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["group_id"] = group_id
        path["user_id"] = user_id
        return self._client.call(
            "groups",
            "add-user",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def create(self, *, name: str) -> ResponseValue:
        """Create a group."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        payload["name"] = name
        return self._client.call(
            "groups",
            "create",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def delete(self, *, group_id: int) -> ResponseValue:
        """Delete a group."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["group_id"] = group_id
        return self._client.call(
            "groups",
            "delete",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def delete_bulk(self, *, ids: builtins.list[JsonValue]) -> ResponseValue:
        """Delete groups in bulk."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        payload["ids"] = ids
        return self._client.call(
            "groups",
            "delete-bulk",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def delete_user(self, *, group_id: int, user_id: int) -> ResponseValue:
        """Delete a user from the group."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["group_id"] = group_id
        path["user_id"] = user_id
        return self._client.call(
            "groups",
            "delete-user",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def edit(self, *, group_id: int, name: str) -> ResponseValue:
        """Edit a group."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["group_id"] = group_id
        payload["name"] = name
        return self._client.call(
            "groups",
            "edit",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def list(self) -> ResponseValue:
        """Returns the group list."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "groups",
            "list",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def list_users(self, *, group_id: int) -> ResponseValue:
        """Return the group user list."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["group_id"] = group_id
        return self._client.call(
            "groups",
            "list-users",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )


class MailAPI(_TypedResource):
    """Typed operations for the mail resource."""

    def change(
        self,
        *,
        smtp_host: str | None = None,
        smtp_port: int | None = None,
        smtp_from: str | None = None,
        smtp_www_host: str | None = None,
        smtp_auth: str,
        smtp_user: str | None = None,
        smtp_pass: str | None = None,
        smtp_enc: str,
    ) -> ResponseValue:
        """Changes the mail server settings."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        if smtp_host is not None:
            payload["smtp_host"] = smtp_host
        if smtp_port is not None:
            payload["smtp_port"] = smtp_port
        if smtp_from is not None:
            payload["smtp_from"] = smtp_from
        if smtp_www_host is not None:
            payload["smtp_www_host"] = smtp_www_host
        payload["smtp_auth"] = smtp_auth
        if smtp_user is not None:
            payload["smtp_user"] = smtp_user
        if smtp_pass is not None:
            payload["smtp_pass"] = smtp_pass
        payload["smtp_enc"] = smtp_enc
        return self._client.call(
            "mail",
            "change",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def view(self) -> ResponseValue:
        """Returns the mail server settings."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "mail",
            "view",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )


class MigrationAPI(_TypedResource):
    """Typed operations for the migration resource."""

    def get_settings(self) -> ResponseValue:
        """Returns the current migration settings."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "migration",
            "get-settings",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def update_settings(
        self,
        *,
        key: str | None = None,
        secret: str | None = None,
        domain: str | None = None,
    ) -> ResponseValue:
        """Changes the migration settings."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        if key is not None:
            payload["key"] = key
        if secret is not None:
            payload["secret"] = secret
        if domain is not None:
            payload["domain"] = domain
        return self._client.call(
            "migration",
            "update-settings",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def status(self) -> ResponseValue:
        """Returns the migration status."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "migration",
            "status",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def start(self) -> ResponseValue:
        """
        Starts or resumes the migration. Before you start the migration, you need
        have the 'key', 'secret' and 'domain' settings set.
        """
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "migration",
            "start",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def stop(self, *, finish: bool | None = None) -> ResponseValue:
        """Finishes or stops the migration."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        if finish is not None:
            query["finish"] = finish
        return self._client.call(
            "migration",
            "stop",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def scan_history(self, *, updatedafter: int | None = None) -> ResponseValue:
        """Returns the scan history migration status."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        if updatedafter is not None:
            query["updatedAfter"] = updatedafter
        return self._client.call(
            "migration",
            "scan-history",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def scan_history_settings(self) -> ResponseValue:
        """Returns the current scan history migration settings."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "migration",
            "scan-history-settings",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def update_scan_history_settings(
        self, *, settings: dict[str, JsonValue] | None = None
    ) -> ResponseValue:
        """Changes the scan history migration settings."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        if settings is not None:
            payload["settings"] = settings
        return self._client.call(
            "migration",
            "update-scan-history-settings",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def start_scan_history_migration(self) -> ResponseValue:
        """Starts the scan history migration process."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "migration",
            "start-scan-history-migration",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def stop_scan_history_migration(self) -> ResponseValue:
        """Stops the scan history migration process."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "migration",
            "stop-scan-history-migration",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def skip_scan_history(self, *, scan_uuid: str) -> ResponseValue:
        """Skips migrating a single scan history item."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["scan_uuid"] = scan_uuid
        return self._client.call(
            "migration",
            "skip-scan-history",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def skip_scan_history_bulk(self, *, ids: builtins.list[JsonValue]) -> ResponseValue:
        """Skips migrating scan history items in bulk."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        payload["ids"] = ids
        return self._client.call(
            "migration",
            "skip-scan-history-bulk",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def reset_scan_history(self, *, scan_uuid: str) -> ResponseValue:
        """
        Resets a scan history item's status to 'not started' so it will be migrated.
        """
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["scan_uuid"] = scan_uuid
        return self._client.call(
            "migration",
            "reset-scan-history",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def reset_scan_history_bulk(
        self, *, ids: builtins.list[JsonValue]
    ) -> ResponseValue:
        """
        Resets the status of the scan history items matching the provided IDs so
        they can be migrated.
        """
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        payload["ids"] = ids
        return self._client.call(
            "migration",
            "reset-scan-history-bulk",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )


class PermissionsAPI(_TypedResource):
    """Typed operations for the permissions resource."""

    def change(
        self, *, object_type: str, object_id: int, request_body: JsonValue
    ) -> ResponseValue:
        """Changes the permissions for an object."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["object_type"] = object_type
        path["object_id"] = object_id
        return self._client.call(
            "permissions",
            "change",
            path=path or None,
            query=query or None,
            payload=payload or None,
            body=request_body,
        )

    def list(self, *, object_type: str, object_id: int) -> ResponseValue:
        """Returns the current object's permissions."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["object_type"] = object_type
        path["object_id"] = object_id
        return self._client.call(
            "permissions",
            "list",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )


class PluginRulesAPI(_TypedResource):
    """Typed operations for the plugin-rules resource."""

    def create(
        self, *, plugin_id: int, type: str, host: str, date: str | None = None
    ) -> ResponseValue:
        """Create a new plugin rule for the current user."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        payload["plugin_id"] = plugin_id
        payload["type"] = type
        payload["host"] = host
        if date is not None:
            payload["date"] = date
        return self._client.call(
            "plugin-rules",
            "create",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def delete(self, *, rule_id: int) -> ResponseValue:
        """Delete a plugin rule."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["rule_id"] = rule_id
        return self._client.call(
            "plugin-rules",
            "delete",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def delete_bulk(self, *, ids: builtins.list[JsonValue]) -> ResponseValue:
        """Delete plugin rules in bulk."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        payload["ids"] = ids
        return self._client.call(
            "plugin-rules",
            "delete-bulk",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def edit(
        self,
        *,
        rule_id: int,
        plugin_id: int,
        type: str,
        host: str,
        date: str | None = None,
    ) -> ResponseValue:
        """Modify a plugin rule for the current user."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["rule_id"] = rule_id
        payload["plugin_id"] = plugin_id
        payload["type"] = type
        payload["host"] = host
        if date is not None:
            payload["date"] = date
        return self._client.call(
            "plugin-rules",
            "edit",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def list(self) -> ResponseValue:
        """Return the current user's plugin rules."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "plugin-rules",
            "list",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def details(self, *, rule_id: int) -> ResponseValue:
        """Returns the details for a given rule."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["rule_id"] = rule_id
        return self._client.call(
            "plugin-rules",
            "details",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )


class PluginsAPI(_TypedResource):
    """Typed operations for the plugins resource."""

    def families(self) -> ResponseValue:
        """Returns the list of plugin families."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "plugins",
            "families",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def family_details(self, *, id: int) -> ResponseValue:
        """Returns the list of plugins in a family."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["id"] = id
        return self._client.call(
            "plugins",
            "family-details",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def plugin_details(self, *, id: int) -> ResponseValue:
        """Returns details for a given plugin."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["id"] = id
        return self._client.call(
            "plugins",
            "plugin-details",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )


class PoliciesAPI(_TypedResource):
    """Typed operations for the policies resource."""

    def configure(self, *, policy_id: int) -> ResponseValue:
        """Changes the parameters of a policy."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["policy_id"] = policy_id
        return self._client.call(
            "policies",
            "configure",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def copy(self, *, policy_id: int) -> ResponseValue:
        """Copy a policy."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["policy_id"] = policy_id
        return self._client.call(
            "policies",
            "copy",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def create(
        self, *, uuid: str, settings: dict[str, JsonValue] | None = None
    ) -> ResponseValue:
        """Create a policy."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        payload["uuid"] = uuid
        if settings is not None:
            payload["settings"] = settings
        return self._client.call(
            "policies",
            "create",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def delete(self, *, policy_id: int) -> ResponseValue:
        """Delete a policy."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["policy_id"] = policy_id
        return self._client.call(
            "policies",
            "delete",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def delete_bulk(self, *, ids: builtins.list[JsonValue]) -> ResponseValue:
        """Delete policies in bulk."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        payload["ids"] = ids
        return self._client.call(
            "policies",
            "delete-bulk",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def details(self, *, policy_id: int) -> ResponseValue:
        """Returns details for the given policy."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["policy_id"] = policy_id
        return self._client.call(
            "policies",
            "details",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def import_(self, *, file: str) -> ResponseValue:
        """
        Import an existing policy uploaded using file: upload (.nessus format only).
        """
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        payload["file"] = file
        return self._client.call(
            "policies",
            "import",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def export(
        self, *, policy_id: int, output_path: str | Path | None = None
    ) -> ResponseValue:
        """Export the given policy."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["policy_id"] = policy_id
        return self._client.call(
            "policies",
            "export",
            path=path or None,
            query=query or None,
            payload=payload or None,
            output_path=output_path,
        )

    def export_token_download(self, *, policy_id: int) -> ResponseValue:
        """Export the given policy for download via a single use token."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["policy_id"] = policy_id
        return self._client.call(
            "policies",
            "export-token-download",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def list(self) -> ResponseValue:
        """Returns the policy list."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "policies",
            "list",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )


class ProfilesAPI(_TypedResource):
    """Typed operations for the profiles resource."""

    def add_profile(
        self,
        *,
        name: str,
        description: str | None = None,
        config: builtins.list[JsonValue],
        config_version: str | None = None,
        config_resources: builtins.list[JsonValue] | None = None,
    ) -> ResponseValue:
        """Add a new agent profile."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        payload["name"] = name
        if description is not None:
            payload["description"] = description
        payload["config"] = config
        if config_version is not None:
            payload["config.version"] = config_version
        if config_resources is not None:
            payload["config.resources"] = config_resources
        return self._client.call(
            "profiles",
            "add-profile",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def add_profile_members(
        self,
        *,
        profile_uuid: str,
        ids: builtins.list[JsonValue] | None = None,
        filters: str | None = None,
    ) -> ResponseValue:
        """Add agent members to an agent profile."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["profile_uuid"] = profile_uuid
        if ids is not None:
            payload["ids"] = ids
        if filters is not None:
            payload["filters"] = filters
        return self._client.call(
            "profiles",
            "add-profile-members",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def delete_profiles(
        self, *, profile_uuids: builtins.list[JsonValue]
    ) -> ResponseValue:
        """Delete agent profile(s)."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        payload["profile_uuids"] = profile_uuids
        return self._client.call(
            "profiles",
            "delete-profiles",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def delete_profile_members(
        self,
        *,
        profile_uuid: str,
        ids: builtins.list[JsonValue] | None = None,
        filters: str | None = None,
    ) -> ResponseValue:
        """Remove agent members from an agent profile."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["profile_uuid"] = profile_uuid
        if ids is not None:
            payload["ids"] = ids
        if filters is not None:
            payload["filters"] = filters
        return self._client.call(
            "profiles",
            "delete-profile-members",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def delete_profile_from_agents(
        self, *, ids: builtins.list[JsonValue] | None = None, filters: str | None = None
    ) -> ResponseValue:
        """Delete profile(s) from agent(s)."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        if ids is not None:
            payload["ids"] = ids
        if filters is not None:
            payload["filters"] = filters
        return self._client.call(
            "profiles",
            "delete-profile-from-agents",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def get_profile(self, *, profile_uuid: str) -> ResponseValue:
        """Returns a specific agent profile."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["profile_uuid"] = profile_uuid
        return self._client.call(
            "profiles",
            "get-profile",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def get_profile_members(self, *, profile_uuid: str) -> ResponseValue:
        """Get the agent membership for an agent profile."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["profile_uuid"] = profile_uuid
        return self._client.call(
            "profiles",
            "get-profile-members",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def list(self) -> ResponseValue:
        """List all agent profiles."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "profiles",
            "list",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def set_profile_for_agent(
        self, *, profile_uuid: str, agent_id: Any
    ) -> ResponseValue:
        """Assign an agent profile to an agent."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["profile_uuid"] = profile_uuid
        path["agent_id"] = agent_id
        return self._client.call(
            "profiles",
            "set-profile-for-agent",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def unset_profile_for_agent(
        self, *, profile_uuid: str, agent_id: Any
    ) -> ResponseValue:
        """Remove agent profile assignment from an agent."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["profile_uuid"] = profile_uuid
        path["agent_id"] = agent_id
        return self._client.call(
            "profiles",
            "unset-profile-for-agent",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def update_profile(
        self,
        *,
        profile_uuid: str,
        name: str,
        description: str | None = None,
        config: builtins.list[JsonValue],
        config_version: str | None = None,
        config_resources: builtins.list[JsonValue] | None = None,
    ) -> ResponseValue:
        """Update an existing agent profile."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["profile_uuid"] = profile_uuid
        payload["name"] = name
        if description is not None:
            payload["description"] = description
        payload["config"] = config
        if config_version is not None:
            payload["config.version"] = config_version
        if config_resources is not None:
            payload["config.resources"] = config_resources
        return self._client.call(
            "profiles",
            "update-profile",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )


class ProxyAPI(_TypedResource):
    """Typed operations for the proxy resource."""

    def change(
        self,
        *,
        proxy: str | None = None,
        proxy_auth: str | None = None,
        proxy_password: str | None = None,
        proxy_port: int | None = None,
        proxy_username: str | None = None,
        user_agent: str | None = None,
    ) -> ResponseValue:
        """Changes the proxy settings."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        if proxy is not None:
            payload["proxy"] = proxy
        if proxy_auth is not None:
            payload["proxy_auth"] = proxy_auth
        if proxy_password is not None:
            payload["proxy_password"] = proxy_password
        if proxy_port is not None:
            payload["proxy_port"] = proxy_port
        if proxy_username is not None:
            payload["proxy_username"] = proxy_username
        if user_agent is not None:
            payload["user_agent"] = user_agent
        return self._client.call(
            "proxy",
            "change",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def view(self) -> ResponseValue:
        """Returns the proxy settings."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "proxy",
            "view",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )


class ReportsAPI(_TypedResource):
    """Typed operations for the reports resource."""

    def list_custom_reports(self) -> ResponseValue:
        """Lists all of a scanners custom reports"""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "reports",
            "list-custom-reports",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def custom_report_details(self, *, template_id: int) -> ResponseValue:
        """Returns details for the given custom report"""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["template_id"] = template_id
        return self._client.call(
            "reports",
            "custom-report-details",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )


class ScannersAPI(_TypedResource):
    """Typed operations for the scanners resource."""

    def control_scans(
        self, *, scanner_id: int, scan_uuid: str, action: str
    ) -> ResponseValue:
        """Allows control of scans that are currently running on a scanner."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["scanner_id"] = scanner_id
        path["scan_uuid"] = scan_uuid
        payload["action"] = action
        return self._client.call(
            "scanners",
            "control-scans",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def delete(self, *, scanner_id: int) -> ResponseValue:
        """Delete and unlink a scanner from Nessus."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["scanner_id"] = scanner_id
        return self._client.call(
            "scanners",
            "delete",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def delete_bulk(self, *, ids: builtins.list[JsonValue]) -> ResponseValue:
        """Delete and unlink a list of scanners from Nessus."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        payload["ids"] = ids
        return self._client.call(
            "scanners",
            "delete-bulk",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def details(self, *, scanner_id: int) -> ResponseValue:
        """Returns details for the given scanner."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["scanner_id"] = scanner_id
        return self._client.call(
            "scanners",
            "details",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def edit(
        self,
        *,
        scanner_id: int,
        force_plugin_update: int | None = None,
        force_ui_update: int | None = None,
        finish_update: int | None = None,
        registration_code: str | None = None,
        aws_update_interval: int | None = None,
    ) -> ResponseValue:
        """Edit the scanner identified by 'scanner_id'."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["scanner_id"] = scanner_id
        if force_plugin_update is not None:
            payload["force_plugin_update"] = force_plugin_update
        if force_ui_update is not None:
            payload["force_ui_update"] = force_ui_update
        if finish_update is not None:
            payload["finish_update"] = finish_update
        if registration_code is not None:
            payload["registration_code"] = registration_code
        if aws_update_interval is not None:
            payload["aws_update_interval"] = aws_update_interval
        return self._client.call(
            "scanners",
            "edit",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def get_aws_targets(self, *, scanner_id: int) -> ResponseValue:
        """
        Returns a list of AWS scan targets if the requested scanner is an Amazon Web
        Services scanner.
        """
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["scanner_id"] = scanner_id
        return self._client.call(
            "scanners",
            "get-aws-targets",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def get_scanner_key(self, *, scanner_id: int) -> ResponseValue:
        """Returns the key of the requested scanner."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["scanner_id"] = scanner_id
        return self._client.call(
            "scanners",
            "get-scanner-key",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def get_scans(self, *, scanner_id: int) -> ResponseValue:
        """Returns a list of scans running on the requested scanner."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["scanner_id"] = scanner_id
        return self._client.call(
            "scanners",
            "get-scans",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def list(self) -> ResponseValue:
        """Returns the scanner list."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "scanners",
            "list",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def toggle_link_state(self, *, scanner_id: int, link: int) -> ResponseValue:
        """
        Enables or disables the link state of the scanner identified by
        'scanner_id'.
        """
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["scanner_id"] = scanner_id
        payload["link"] = link
        return self._client.call(
            "scanners",
            "toggle-link-state",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )


class ScansAPI(_TypedResource):
    """Typed operations for the scans resource."""

    def attachment_prepare(
        self, *, scan_id: int, attachment_id: int, history_id: int | None = None
    ) -> ResponseValue:
        """
        Returns a single-use scan attachment token for the scan and attachment IDs.
        """
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["scan_id"] = scan_id
        path["attachment_id"] = attachment_id
        if history_id is not None:
            payload["history_id"] = history_id
        return self._client.call(
            "scans",
            "attachment-prepare",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def configure(
        self,
        *,
        scan_id: int,
        uuid: str | None = None,
        settings: dict[str, JsonValue] | None = None,
    ) -> ResponseValue:
        """Changes the schedule or policy parameters of a scan."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["scan_id"] = scan_id
        if uuid is not None:
            payload["uuid"] = uuid
        if settings is not None:
            payload["settings"] = settings
        return self._client.call(
            "scans",
            "configure",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def copy(
        self, *, scan_id: int, folder_id: int | None = None, name: str | None = None
    ) -> ResponseValue:
        """Copies the given scan."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["scan_id"] = scan_id
        if folder_id is not None:
            payload["folder_id"] = folder_id
        if name is not None:
            payload["name"] = name
        return self._client.call(
            "scans",
            "copy",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def create(
        self, *, uuid: str, settings: dict[str, JsonValue] | None = None
    ) -> ResponseValue:
        """Create a scan."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        payload["uuid"] = uuid
        if settings is not None:
            payload["settings"] = settings
        return self._client.call(
            "scans",
            "create",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def delete(self, *, scan_id: int) -> ResponseValue:
        """
        Delete a scan. NOTE: Scans in running, paused or stopping states can not be
        deleted.
        """
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["scan_id"] = scan_id
        return self._client.call(
            "scans",
            "delete",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def delete_bulk(self, *, ids: builtins.list[JsonValue]) -> ResponseValue:
        """
        Delete scans in bulk. NOTE: Scans in running, paused or stopping states can
        not be deleted.
        """
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        payload["ids"] = ids
        return self._client.call(
            "scans",
            "delete-bulk",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def delete_history(self, *, scan_id: int, history_id: int) -> ResponseValue:
        """Delete historical results from a scan."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["scan_id"] = scan_id
        path["history_id"] = history_id
        return self._client.call(
            "scans",
            "delete-history",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def details(
        self, *, scan_id: int, history_id: int | None = None, limit: int | None = None
    ) -> ResponseValue:
        """Returns details for the given scan."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["scan_id"] = scan_id
        if history_id is not None:
            query["history_id"] = history_id
        if limit is not None:
            query["limit"] = limit
        return self._client.call(
            "scans",
            "details",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def details_filters(self) -> ResponseValue:
        """Returns the filters available for scan details."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "scans",
            "details-filters",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def export_formats(
        self, *, scan_id: int, schedule_id: int | None = None
    ) -> ResponseValue:
        """Returns available export formats and report options."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["scan_id"] = scan_id
        if schedule_id is not None:
            query["schedule_id"] = schedule_id
        return self._client.call(
            "scans",
            "export-formats",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def export_download(
        self, *, scan_id: int, file_id: int, output_path: str | Path | None = None
    ) -> ResponseValue:
        """Download an exported scan."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["scan_id"] = scan_id
        path["file_id"] = file_id
        return self._client.call(
            "scans",
            "export-download",
            path=path or None,
            query=query or None,
            payload=payload or None,
            output_path=output_path,
        )

    def export_request(
        self,
        *,
        scan_id: int,
        history_id: int | None = None,
        format: str,
        password: str | None = None,
        chapters: str | None = None,
        filters: dict[str, JsonValue] | None = None,
        filter_search_type: str | None = None,
        reportcontents_formattingoptions_page_breaks: bool | None = None,
        reportcontents_hostsections_scan_information: bool | None = None,
        reportcontents_hostsections_host_information: bool | None = None,
        reportcontents_vulnerabilitysections_synopsis: bool | None = None,
        reportcontents_vulnerabilitysections_description: bool | None = None,
        reportcontents_vulnerabilitysections_see_also: bool | None = None,
        reportcontents_vulnerabilitysections_solution: bool | None = None,
        reportcontents_vulnerabilitysections_risk_factor: bool | None = None,
        reportcontents_vulnerabilitysections_cvss4_base_score: bool | None = None,
        reportcontents_vulnerabilitysections_cvss4_bt_score: bool | None = None,
        reportcontents_vulnerabilitysections_cvss3_base_score: bool | None = None,
        reportcontents_vulnerabilitysections_cvss3_temporal_score: bool | None = None,
        reportcontents_vulnerabilitysections_cvss_base_score: bool | None = None,
        reportcontents_vulnerabilitysections_cvss_temporal_score: bool | None = None,
        reportcontents_vulnerabilitysections_stig_severity: bool | None = None,
        reportcontents_vulnerabilitysections_references: bool | None = None,
        reportcontents_vulnerabilitysections_exploitable_with: bool | None = None,
        reportcontents_vulnerabilitysections_plugin_information: bool | None = None,
        reportcontents_vulnerabilitysections_plugin_output: bool | None = None,
        reportcontents_csvcolumns_id: bool | None = None,
        reportcontents_csvcolumns_cve: bool | None = None,
        reportcontents_csvcolumns_cvss: bool | None = None,
        reportcontents_csvcolumns_risk: bool | None = None,
        reportcontents_csvcolumns_hostname: bool | None = None,
        reportcontents_csvcolumns_protocol: bool | None = None,
        reportcontents_csvcolumns_port: bool | None = None,
        reportcontents_csvcolumns_plugin_name: bool | None = None,
        reportcontents_csvcolumns_synopsis: bool | None = None,
        reportcontents_csvcolumns_description: bool | None = None,
        reportcontents_csvcolumns_solution: bool | None = None,
        reportcontents_csvcolumns_see_also: bool | None = None,
        reportcontents_csvcolumns_plugin_output: bool | None = None,
        reportcontents_csvcolumns_stig_severity: bool | None = None,
        reportcontents_csvcolumns_cvss3_base_score: bool | None = None,
        reportcontents_csvcolumns_cvss_temporal_score: bool | None = None,
        reportcontents_csvcolumns_cvss3_temporal_score: bool | None = None,
        reportcontents_csvcolumns_vpr_score: bool | None = None,
        reportcontents_csvcolumns_risk_factor: bool | None = None,
        reportcontents_csvcolumns_references: bool | None = None,
        reportcontents_csvcolumns_plugin_information: bool | None = None,
        reportcontents_csvcolumns_exploitable_with: bool | None = None,
        template_id: int,
    ) -> ResponseValue:
        """
        Export the given scan. Once requested, the file can be downloaded using the
        token download method upon receiving a "ready" status from the token status
        method. You can also use the older export status and export download
        methods.NOTE: In cluster environments, Tenable.sc is the aggregation point
        for scan data, not the cluster parent node. The cluster nodes are not
        intended to have export requests made of them.
        """
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["scan_id"] = scan_id
        if history_id is not None:
            query["history_id"] = history_id
        payload["format"] = format
        if password is not None:
            payload["password"] = password
        if chapters is not None:
            payload["chapters"] = chapters
        if filters is not None:
            payload["filters"] = filters
        if filter_search_type is not None:
            payload["filter.search_type"] = filter_search_type
        if reportcontents_formattingoptions_page_breaks is not None:
            payload["reportContents.formattingOptions.page_breaks"] = (
                reportcontents_formattingoptions_page_breaks
            )
        if reportcontents_hostsections_scan_information is not None:
            payload["reportContents.hostSections.scan_information"] = (
                reportcontents_hostsections_scan_information
            )
        if reportcontents_hostsections_host_information is not None:
            payload["reportContents.hostSections.host_information"] = (
                reportcontents_hostsections_host_information
            )
        if reportcontents_vulnerabilitysections_synopsis is not None:
            payload["reportContents.vulnerabilitySections.synopsis"] = (
                reportcontents_vulnerabilitysections_synopsis
            )
        if reportcontents_vulnerabilitysections_description is not None:
            payload["reportContents.vulnerabilitySections.description"] = (
                reportcontents_vulnerabilitysections_description
            )
        if reportcontents_vulnerabilitysections_see_also is not None:
            payload["reportContents.vulnerabilitySections.see_also"] = (
                reportcontents_vulnerabilitysections_see_also
            )
        if reportcontents_vulnerabilitysections_solution is not None:
            payload["reportContents.vulnerabilitySections.solution"] = (
                reportcontents_vulnerabilitysections_solution
            )
        if reportcontents_vulnerabilitysections_risk_factor is not None:
            payload["reportContents.vulnerabilitySections.risk_factor"] = (
                reportcontents_vulnerabilitysections_risk_factor
            )
        if reportcontents_vulnerabilitysections_cvss4_base_score is not None:
            payload["reportContents.vulnerabilitySections.cvss4_base_score"] = (
                reportcontents_vulnerabilitysections_cvss4_base_score
            )
        if reportcontents_vulnerabilitysections_cvss4_bt_score is not None:
            payload["reportContents.vulnerabilitySections.cvss4_bt_score"] = (
                reportcontents_vulnerabilitysections_cvss4_bt_score
            )
        if reportcontents_vulnerabilitysections_cvss3_base_score is not None:
            payload["reportContents.vulnerabilitySections.cvss3_base_score"] = (
                reportcontents_vulnerabilitysections_cvss3_base_score
            )
        if reportcontents_vulnerabilitysections_cvss3_temporal_score is not None:
            payload["reportContents.vulnerabilitySections.cvss3_temporal_score"] = (
                reportcontents_vulnerabilitysections_cvss3_temporal_score
            )
        if reportcontents_vulnerabilitysections_cvss_base_score is not None:
            payload["reportContents.vulnerabilitySections.cvss_base_score"] = (
                reportcontents_vulnerabilitysections_cvss_base_score
            )
        if reportcontents_vulnerabilitysections_cvss_temporal_score is not None:
            payload["reportContents.vulnerabilitySections.cvss_temporal_score"] = (
                reportcontents_vulnerabilitysections_cvss_temporal_score
            )
        if reportcontents_vulnerabilitysections_stig_severity is not None:
            payload["reportContents.vulnerabilitySections.stig_severity"] = (
                reportcontents_vulnerabilitysections_stig_severity
            )
        if reportcontents_vulnerabilitysections_references is not None:
            payload["reportContents.vulnerabilitySections.references"] = (
                reportcontents_vulnerabilitysections_references
            )
        if reportcontents_vulnerabilitysections_exploitable_with is not None:
            payload["reportContents.vulnerabilitySections.exploitable_with"] = (
                reportcontents_vulnerabilitysections_exploitable_with
            )
        if reportcontents_vulnerabilitysections_plugin_information is not None:
            payload["reportContents.vulnerabilitySections.plugin_information"] = (
                reportcontents_vulnerabilitysections_plugin_information
            )
        if reportcontents_vulnerabilitysections_plugin_output is not None:
            payload["reportContents.vulnerabilitySections.plugin_output"] = (
                reportcontents_vulnerabilitysections_plugin_output
            )
        if reportcontents_csvcolumns_id is not None:
            payload["reportContents.csvColumns.id"] = reportcontents_csvcolumns_id
        if reportcontents_csvcolumns_cve is not None:
            payload["reportContents.csvColumns.cve"] = reportcontents_csvcolumns_cve
        if reportcontents_csvcolumns_cvss is not None:
            payload["reportContents.csvColumns.cvss"] = reportcontents_csvcolumns_cvss
        if reportcontents_csvcolumns_risk is not None:
            payload["reportContents.csvColumns.risk"] = reportcontents_csvcolumns_risk
        if reportcontents_csvcolumns_hostname is not None:
            payload["reportContents.csvColumns.hostname"] = (
                reportcontents_csvcolumns_hostname
            )
        if reportcontents_csvcolumns_protocol is not None:
            payload["reportContents.csvColumns.protocol"] = (
                reportcontents_csvcolumns_protocol
            )
        if reportcontents_csvcolumns_port is not None:
            payload["reportContents.csvColumns.port"] = reportcontents_csvcolumns_port
        if reportcontents_csvcolumns_plugin_name is not None:
            payload["reportContents.csvColumns.plugin_name"] = (
                reportcontents_csvcolumns_plugin_name
            )
        if reportcontents_csvcolumns_synopsis is not None:
            payload["reportContents.csvColumns.synopsis"] = (
                reportcontents_csvcolumns_synopsis
            )
        if reportcontents_csvcolumns_description is not None:
            payload["reportContents.csvColumns.description"] = (
                reportcontents_csvcolumns_description
            )
        if reportcontents_csvcolumns_solution is not None:
            payload["reportContents.csvColumns.solution"] = (
                reportcontents_csvcolumns_solution
            )
        if reportcontents_csvcolumns_see_also is not None:
            payload["reportContents.csvColumns.see_also"] = (
                reportcontents_csvcolumns_see_also
            )
        if reportcontents_csvcolumns_plugin_output is not None:
            payload["reportContents.csvColumns.plugin_output"] = (
                reportcontents_csvcolumns_plugin_output
            )
        if reportcontents_csvcolumns_stig_severity is not None:
            payload["reportContents.csvColumns.stig_severity"] = (
                reportcontents_csvcolumns_stig_severity
            )
        if reportcontents_csvcolumns_cvss3_base_score is not None:
            payload["reportContents.csvColumns.cvss3_base_score"] = (
                reportcontents_csvcolumns_cvss3_base_score
            )
        if reportcontents_csvcolumns_cvss_temporal_score is not None:
            payload["reportContents.csvColumns.cvss_temporal_score"] = (
                reportcontents_csvcolumns_cvss_temporal_score
            )
        if reportcontents_csvcolumns_cvss3_temporal_score is not None:
            payload["reportContents.csvColumns.cvss3_temporal_score"] = (
                reportcontents_csvcolumns_cvss3_temporal_score
            )
        if reportcontents_csvcolumns_vpr_score is not None:
            payload["reportContents.csvColumns.vpr_score"] = (
                reportcontents_csvcolumns_vpr_score
            )
        if reportcontents_csvcolumns_risk_factor is not None:
            payload["reportContents.csvColumns.risk_factor"] = (
                reportcontents_csvcolumns_risk_factor
            )
        if reportcontents_csvcolumns_references is not None:
            payload["reportContents.csvColumns.references"] = (
                reportcontents_csvcolumns_references
            )
        if reportcontents_csvcolumns_plugin_information is not None:
            payload["reportContents.csvColumns.plugin_information"] = (
                reportcontents_csvcolumns_plugin_information
            )
        if reportcontents_csvcolumns_exploitable_with is not None:
            payload["reportContents.csvColumns.exploitable_with"] = (
                reportcontents_csvcolumns_exploitable_with
            )
        payload["template_id"] = template_id
        return self._client.call(
            "scans",
            "export-request",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def export_status(self, *, scan_id: int, file_id: int) -> ResponseValue:
        """
        Check the file status of an exported scan. When an export has been
        requested, it is necessary to poll this endpoint until a "ready" status is
        returned, at which point the file is complete and can be downloaded using
        the export download endpoint.
        """
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["scan_id"] = scan_id
        path["file_id"] = file_id
        return self._client.call(
            "scans",
            "export-status",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def host_details(
        self, *, scan_id: int, host_id: int, history_id: int | None = None
    ) -> ResponseValue:
        """Returns details for the given host."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["scan_id"] = scan_id
        path["host_id"] = host_id
        if history_id is not None:
            query["history_id"] = history_id
        return self._client.call(
            "scans",
            "host-details",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def import_(
        self, *, file: str, folder_id: int | None = None, password: str | None = None
    ) -> ResponseValue:
        """Import an existing scan uploaded using file: upload."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        payload["file"] = file
        if folder_id is not None:
            payload["folder_id"] = folder_id
        if password is not None:
            payload["password"] = password
        return self._client.call(
            "scans",
            "import",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def kill(self, *, scan_id: int) -> ResponseValue:
        """
        For use on scans from the local scanner only, "kill" terminates a scan
        faster than "stop". All in-progress plugins are terminated. A scan can be
        killed with the scan in any state.
        """
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["scan_id"] = scan_id
        return self._client.call(
            "scans",
            "kill",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def launch(
        self, *, scan_id: int, alt_targets: builtins.list[JsonValue] | None = None
    ) -> ResponseValue:
        """Launches a scan."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["scan_id"] = scan_id
        if alt_targets is not None:
            payload["alt_targets"] = alt_targets
        return self._client.call(
            "scans",
            "launch",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def list(
        self, *, folder_id: int | None = None, last_modification_date: int | None = None
    ) -> ResponseValue:
        """Returns the scan list."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        if folder_id is not None:
            payload["folder_id"] = folder_id
        if last_modification_date is not None:
            payload["last_modification_date"] = last_modification_date
        return self._client.call(
            "scans",
            "list",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def pause(self, *, scan_id: int) -> ResponseValue:
        """Pauses a scan."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["scan_id"] = scan_id
        return self._client.call(
            "scans",
            "pause",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def plugin_output(
        self,
        *,
        scan_id: int,
        host_id: int,
        plugin_id: int,
        history_id: int | None = None,
    ) -> ResponseValue:
        """Returns the output for a given plugin."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["scan_id"] = scan_id
        path["host_id"] = host_id
        path["plugin_id"] = plugin_id
        if history_id is not None:
            query["history_id"] = history_id
        return self._client.call(
            "scans",
            "plugin-output",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def read_status(self, *, scan_id: int, read: bool) -> ResponseValue:
        """Changes the status of a scan."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["scan_id"] = scan_id
        payload["read"] = read
        return self._client.call(
            "scans",
            "read-status",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def resume(self, *, scan_id: int) -> ResponseValue:
        """Resumes a scan."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["scan_id"] = scan_id
        return self._client.call(
            "scans",
            "resume",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def schedule(self, *, scan_id: int, enabled: bool) -> ResponseValue:
        """Enables or disables a scan schedule."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["scan_id"] = scan_id
        payload["enabled"] = enabled
        return self._client.call(
            "scans",
            "schedule",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def stop(self, *, scan_id: int) -> ResponseValue:
        """Stops a scan."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["scan_id"] = scan_id
        return self._client.call(
            "scans",
            "stop",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def timezones(self) -> ResponseValue:
        """Returns the timezone list for creating a scan."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "scans",
            "timezones",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )


class ServerAPI(_TypedResource):
    """Typed operations for the server resource."""

    def properties(self) -> ResponseValue:
        """
        Returns the server version and other properties. Nessus build and version
        numbers are only available with an established session.
        """
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "server",
            "properties",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def status(self) -> ResponseValue:
        """Returns the server status."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "server",
            "status",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def restart(
        self,
        *,
        reason: str | None = None,
        soft: bool | None = None,
        unlink: bool | None = None,
        when_idle: bool | None = None,
    ) -> ResponseValue:
        """Restarts the Nessus service and/or web server."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        if reason is not None:
            payload["reason"] = reason
        if soft is not None:
            payload["soft"] = soft
        if unlink is not None:
            payload["unlink"] = unlink
        if when_idle is not None:
            payload["when_idle"] = when_idle
        return self._client.call(
            "server",
            "restart",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )


class SessionAPI(_TypedResource):
    """Typed operations for the session resource."""

    def create(self, *, username: str, password: str) -> ResponseValue:
        """
        Create a new session token for the given user. Certificate based logins
        require no parameters.
        """
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        payload["username"] = username
        payload["password"] = password
        return self._client.call(
            "session",
            "create",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def destroy(self) -> ResponseValue:
        """Logs the current user out and destroys the session."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "session",
            "destroy",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def edit(
        self, *, name: str | None = None, email: str | None = None
    ) -> ResponseValue:
        """Changes settings for the current user."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        if name is not None:
            payload["name"] = name
        if email is not None:
            payload["email"] = email
        return self._client.call(
            "session",
            "edit",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def get(self) -> ResponseValue:
        """Returns the user session data."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "session",
            "get",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def password(self, *, password: str, current_password: str) -> ResponseValue:
        """Changes password for the current user."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        payload["password"] = password
        payload["current_password"] = current_password
        return self._client.call(
            "session",
            "password",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def keys(self) -> ResponseValue:
        """Generates API Keys for the current user."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "session",
            "keys",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )


class SettingsAPI(_TypedResource):
    """Typed operations for the settings resource."""

    def health_alert_list(
        self, *, end_time: int | None = None, start_time: int | None = None
    ) -> ResponseValue:
        """
        A list of alerts created by the scanner regarding its overall health.
        """
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        if end_time is not None:
            query["end_time"] = end_time
        if start_time is not None:
            query["start_time"] = start_time
        return self._client.call(
            "settings",
            "health-alert-list",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def health_stats(
        self,
        *,
        end_time: int | None = None,
        start_time: int | None = None,
        count: int | None = None,
    ) -> ResponseValue:
        """
        A historical record of scanner statistics based on metrics such as memory
        usage, data sent/received, etc.
        """
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        if end_time is not None:
            query["end_time"] = end_time
        if start_time is not None:
            query["start_time"] = start_time
        if count is not None:
            query["count"] = count
        return self._client.call(
            "settings",
            "health-stats",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def list_advanced(self) -> ResponseValue:
        """
        Lists the advanced settings, its configurations, and its current values.
        """
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "settings",
            "list-advanced",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def modify_advanced(
        self,
        *,
        setting_0_action: str,
        setting_0_id: str | None = None,
        setting_0_name: str,
        setting_0_value: str | None = None,
    ) -> ResponseValue:
        """
        A CRUD interface for adding, editing, and deleting custom advanced settings.
        In addition, users can edit or reset Tenable-provided advanced settings.
        """
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        payload["setting.0.action"] = setting_0_action
        if setting_0_id is not None:
            payload["setting.0.id"] = setting_0_id
        payload["setting.0.name"] = setting_0_name
        if setting_0_value is not None:
            payload["setting.0.value"] = setting_0_value
        return self._client.call(
            "settings",
            "modify-advanced",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def modify_plugin_detail_locale(
        self,
        *,
        enabled: bool | None = None,
        default_plugin_locale: str | None = None,
        current: Any | None = None,
    ) -> ResponseValue:
        """
        The locale (language) in which plugin details appear in the Tenable Nessus
        user interface and reports.
        """
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        if enabled is not None:
            payload["enabled"] = enabled
        if default_plugin_locale is not None:
            payload["default_plugin_locale"] = default_plugin_locale
        if current is not None:
            payload["current"] = current
        return self._client.call(
            "settings",
            "modify-plugin-detail-locale",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def get_plugin_detail_locale(self) -> ResponseValue:
        """Locale plugin details."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "settings",
            "get-plugin-detail-locale",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )


class SoftwareUpdateAPI(_TypedResource):
    """Typed operations for the software-update resource."""

    def schedule(self) -> ResponseValue:
        """Schedules a software update for all components."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "software-update",
            "schedule",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def settings(
        self,
        *,
        update: str,
        custom_host: str | None = None,
        auto_update_delay: Any | None = None,
    ) -> ResponseValue:
        """Changes the software update settings"""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        payload["update"] = update
        if custom_host is not None:
            payload["custom_host"] = custom_host
        if auto_update_delay is not None:
            payload["auto_update_delay"] = auto_update_delay
        return self._client.call(
            "software-update",
            "settings",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )


class TerrascanAPI(_TypedResource):
    """Typed operations for the terrascan resource."""

    def get_info(self) -> ResponseValue:
        """Returns information about Terrascan"""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "terrascan",
            "get-info",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def set_desired(self, *, terrascan: bool) -> ResponseValue:
        """Set whether to install or remove Terrascan."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        payload["terrascan"] = terrascan
        return self._client.call(
            "terrascan",
            "set-desired",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def download(self) -> ResponseValue:
        """Download Terrascan"""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "terrascan",
            "download",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def get_config(self, *, config_id: int) -> ResponseValue:
        """Get configuration"""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["config_id"] = config_id
        return self._client.call(
            "terrascan",
            "get-config",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def save_config(
        self, *, config: Any, name: str, config_id: int | None = None
    ) -> ResponseValue:
        """Save a configuration"""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        payload["config"] = config
        payload["name"] = name
        if config_id is not None:
            payload["config_id"] = config_id
        return self._client.call(
            "terrascan",
            "save-config",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def delete_config(self, *, config_id: int) -> ResponseValue:
        """Delete configuration"""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["config_id"] = config_id
        return self._client.call(
            "terrascan",
            "delete-config",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def edit_config(self, *, config_id: int) -> ResponseValue:
        """Saves configuration"""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["config_id"] = config_id
        return self._client.call(
            "terrascan",
            "edit-config",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def get_configs(self) -> ResponseValue:
        """List of configurations"""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "terrascan",
            "get-configs",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def delete_configs(self, *, config_id: int) -> ResponseValue:
        """Delete configurations"""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        payload["config_id"] = config_id
        return self._client.call(
            "terrascan",
            "delete-configs",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def get_default_config(self) -> ResponseValue:
        """Get default configuration"""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "terrascan",
            "get-default-config",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def get_scans(self, *, config_id: int, scan_id: int | None = None) -> ResponseValue:
        """List of Terrascan scans"""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["config_id"] = config_id
        if scan_id is not None:
            query["scan_id"] = scan_id
        return self._client.call(
            "terrascan",
            "get-scans",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def launch_scan(self, *, config_id: int) -> ResponseValue:
        """Launch Terrascan scan"""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["config_id"] = config_id
        return self._client.call(
            "terrascan",
            "launch-scan",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def delete_scan(self, *, scan_ids: builtins.list[JsonValue]) -> ResponseValue:
        """Delete Terrascan Scan"""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        payload["scan_ids"] = scan_ids
        return self._client.call(
            "terrascan",
            "delete-scan",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def download_scan_result(
        self, *, config_id: int, scan_id: int, format: str
    ) -> ResponseValue:
        """Download Terrascan scan results"""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["config_id"] = config_id
        path["scan_id"] = scan_id
        path["format"] = format
        return self._client.call(
            "terrascan",
            "download-scan-result",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def download_scan_result_command_output(
        self, *, config_id: int, scan_id: int
    ) -> ResponseValue:
        """Download Terrascan scan result command output"""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["config_id"] = config_id
        path["scan_id"] = scan_id
        return self._client.call(
            "terrascan",
            "download-scan-result-command-output",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )


class TokensAPI(_TypedResource):
    """Typed operations for the tokens resource."""

    def status(self, *, token: str) -> ResponseValue:
        """Gets the status of a token; used for token based downloads."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["token"] = token
        return self._client.call(
            "tokens",
            "status",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def download(self, *, token: str) -> ResponseValue:
        """Downloads the payload for the given token."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["token"] = token
        return self._client.call(
            "tokens",
            "download",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )


class UsersAPI(_TypedResource):
    """Typed operations for the users resource."""

    def create(
        self,
        *,
        username: str,
        password: str,
        permissions: str,
        name: str | None = None,
        email: str | None = None,
        type: str,
    ) -> ResponseValue:
        """Create a new user."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        payload["username"] = username
        payload["password"] = password
        payload["permissions"] = permissions
        if name is not None:
            payload["name"] = name
        if email is not None:
            payload["email"] = email
        payload["type"] = type
        return self._client.call(
            "users",
            "create",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def delete(self, *, user_id: int) -> ResponseValue:
        """Delete a user."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["user_id"] = user_id
        return self._client.call(
            "users",
            "delete",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def delete_bulk(self, *, ids: builtins.list[JsonValue]) -> ResponseValue:
        """Delete users in bulk."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        payload["ids"] = ids
        return self._client.call(
            "users",
            "delete-bulk",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def details(self, *, user_id: int) -> ResponseValue:
        """Returns details for the given user."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["user_id"] = user_id
        return self._client.call(
            "users",
            "details",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def edit(
        self,
        *,
        user_id: int,
        permissions: str,
        name: str | None = None,
        email: str | None = None,
    ) -> ResponseValue:
        """Edits an existing user."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["user_id"] = user_id
        payload["permissions"] = permissions
        if name is not None:
            payload["name"] = name
        if email is not None:
            payload["email"] = email
        return self._client.call(
            "users",
            "edit",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def list(self) -> ResponseValue:
        """Returns the user list."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "users",
            "list",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def password(
        self, *, user_id: int, current_password: str, password: str
    ) -> ResponseValue:
        """Changes the password for the given user."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["user_id"] = user_id
        payload["current_password"] = current_password
        payload["password"] = password
        return self._client.call(
            "users",
            "password",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )

    def keys(self, *, user_id: int) -> ResponseValue:
        """Generates the API Keys for the given user."""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        path["user_id"] = user_id
        return self._client.call(
            "users",
            "keys",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )


class WasAPI(_TypedResource):
    """Typed operations for the was resource."""

    def image_upload(self, *, file_path: str | Path) -> ResponseValue:
        """Uploads a WAS Docker &reg; tarball image"""
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "was",
            "image-upload",
            path=path or None,
            query=query or None,
            payload=payload or None,
            file_path=file_path,
        )

    def image_ingest(self) -> ResponseValue:
        """
        Ingest the WAS Docker &reg; tarball image that was uploaded using was:
        image-upload
        """
        path: dict[str, JsonValue] = {}
        query: dict[str, JsonValue] = {}
        payload: dict[str, JsonValue] = {}
        return self._client.call(
            "was",
            "image-ingest",
            path=path or None,
            query=query or None,
            payload=payload or None,
        )


class TypedNessusClient(NessusClient):
    """NessusClient with generated, statically discoverable resources."""

    @property
    def agent_groups(self) -> AgentGroupsAPI:
        return AgentGroupsAPI(self)

    @property
    def agents(self) -> AgentsAPI:
        return AgentsAPI(self)

    @property
    def editor(self) -> EditorAPI:
        return EditorAPI(self)

    @property
    def file(self) -> FileAPI:
        return FileAPI(self)

    @property
    def folders(self) -> FoldersAPI:
        return FoldersAPI(self)

    @property
    def groups(self) -> GroupsAPI:
        return GroupsAPI(self)

    @property
    def mail(self) -> MailAPI:
        return MailAPI(self)

    @property
    def migration(self) -> MigrationAPI:
        return MigrationAPI(self)

    @property
    def permissions(self) -> PermissionsAPI:
        return PermissionsAPI(self)

    @property
    def plugin_rules(self) -> PluginRulesAPI:
        return PluginRulesAPI(self)

    @property
    def plugins(self) -> PluginsAPI:
        return PluginsAPI(self)

    @property
    def policies(self) -> PoliciesAPI:
        return PoliciesAPI(self)

    @property
    def profiles(self) -> ProfilesAPI:
        return ProfilesAPI(self)

    @property
    def proxy(self) -> ProxyAPI:
        return ProxyAPI(self)

    @property
    def reports(self) -> ReportsAPI:
        return ReportsAPI(self)

    @property
    def scanners(self) -> ScannersAPI:
        return ScannersAPI(self)

    @property
    def scans(self) -> ScansAPI:
        return ScansAPI(self)

    @property
    def server(self) -> ServerAPI:
        return ServerAPI(self)

    @property
    def session(self) -> SessionAPI:
        return SessionAPI(self)

    @property
    def settings(self) -> SettingsAPI:
        return SettingsAPI(self)

    @property
    def software_update(self) -> SoftwareUpdateAPI:
        return SoftwareUpdateAPI(self)

    @property
    def terrascan(self) -> TerrascanAPI:
        return TerrascanAPI(self)

    @property
    def tokens(self) -> TokensAPI:
        return TokensAPI(self)

    @property
    def users(self) -> UsersAPI:
        return UsersAPI(self)

    @property
    def was(self) -> WasAPI:
        return WasAPI(self)


__all__ = [
    "TypedNessusClient",
    "AgentGroupsAPI",
    "AgentsAPI",
    "EditorAPI",
    "FileAPI",
    "FoldersAPI",
    "GroupsAPI",
    "MailAPI",
    "MigrationAPI",
    "PermissionsAPI",
    "PluginRulesAPI",
    "PluginsAPI",
    "PoliciesAPI",
    "ProfilesAPI",
    "ProxyAPI",
    "ReportsAPI",
    "ScannersAPI",
    "ScansAPI",
    "ServerAPI",
    "SessionAPI",
    "SettingsAPI",
    "SoftwareUpdateAPI",
    "TerrascanAPI",
    "TokensAPI",
    "UsersAPI",
    "WasAPI",
]
