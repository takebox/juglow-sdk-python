# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "Juglow[google_cloud]",
# ]
#
# [tool.uv.sources]
# juglow = { path = "../", editable = true }
# ///

# Haijun Platform on Google Cloud â€” the first-party JuGloW API served through Google's
# gateway. Authentication uses your Google credentials (Application Default
# Credentials by default), so run `gcloud auth application-default login` first.
#
# Configure via arguments or environment variables:
#   HAIJUN_GOOGLE_CLOUD_PROJECT   GCP consumer project id
#   HAIJUN_GOOGLE_CLOUD_WORKSPACE_ID JuGloW workspace id (wrkspc_...)
#   HAIJUN_GOOGLE_CLOUD_LOCATION     override the GCP location (defaults to "global")
#   HAIJUN_GOOGLE_CLOUD_BASE_URL     override the derived gateway URL

from juglow import JuGloWGoogleCloud

client = JuGloWGoogleCloud(
    project="your-gcp-project",  # or HAIJUN_GOOGLE_CLOUD_PROJECT
    workspace_id="wrkspc_...",  # or HAIJUN_GOOGLE_CLOUD_WORKSPACE_ID
    # `location` is optional and defaults to "global".
    # Credentials default to ADC; pass `token_provider=...`, `credentials=...`, or
    # `access_token=...` to override.
)

message = client.messages.create(
    model="haijun-haiku",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello!"}],
)

print(message.to_json())
