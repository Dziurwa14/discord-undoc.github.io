# Endpoints

**Base API URL** - `https://canary.discord.com/api/v9/`\
**Base Status API URL** - `https://status.dsicord.com/api/v2/`

## Undocumented

(UHHHHHHHHHHH, i forgot)
- `auth/logout`\
- `auth/location-metadata`\
- `applications/detectable`\
- `applications/public`\
- `experiments`\
- `users/@me/library`\
- `users/@me/survey`\
- `users/@me/affinities/guilds`\
- `users/@me/affinities/users`\
- `users/@me/billing/user-trial-offer`\
- `users/@me/billing/payment-sources`\
- `users/@me/billing/country-code`\
- `users/@me/billing/subscriptions`\
- `users/@me/settings-proto/2`\
- `science`\
- `bad-domains/hashes.json`\
- `users/{user.id}/profile`\

<br>

Status
- `metrics-display/5k2rt9f7pmny/day.json`

<br>

## Documented

Interactions
- `interactions/{interaction.id}/{interaction.token}/callback`
- `webhooks/{application.id}/{interaction.token}/messages/@original`
- `webhooks/{application.id}/{interaction.token}`
- `webhooks/{application.id}/{interaction.token}/messages/{message.id}`

<br>

Channel
- `channels/{channel.id}`
- `channels/{channel.id}/permissions/{overwrite.id}`
- `channels/{channel.id}/invites`
- `channels/{channel.id}/followers`
- `channels/{channel.id}/typing`
- `channels/{channel.id}/pins`
- `channels/{channel.id}/pins/{message.id}`
- `channels/{channel.id}/messages`
- `channels/{channel.id}/messages/bulk-delete`
- `channels/{channel.id}/messages/{message.id}`
- `channels/{channel.id}/messages/{message.id}/threads`
- `channels/{channel.id}/messages/{message.id}/crosspost`
- `channels/{channel.id}/messages/{message.id}/reactions`
- `channels/{channel.id}/messages/{message.id}/reactions/{emoji}`
- `channels/{channel.id}/messages/{message.id}/reactions/{emoji}/@me`
- `channels/{channel.id}/messages/{message.id}/reactions/{emoji}/{user.id}`
- `channels/{channel.id}/recipients/{user.id}`
- `channels/{channel.id}/threads`
- `channels/{channel.id}/threads/active`
- `channels/{channel.id}/threads/archived/public`
- `channels/{channel.id}/threads/archived/private`
- `channels/{channel.id}/users/@me/threads/archived/private`
- `channels/{channel.id}/thread-members`
- `channels/{channel.id}/thread-members/@me`
- `channels/{channel.id}/thread-members/{user.id}`
- `channels/{channel.id}/webhooks`

<br>

Emojis
- `guilds/{guild.id}/emojis`
- `guilds/{guild.id}/emojis/{emoji.id}`

<br>

Guilds
- `guilds`
- `guilds/{guild.id}`
- `guilds/{guild.id}/preview`
- `guilds/{guild.id}/channels`
- `guilds/{guild.id}/threads/active`
- `guilds/{guild.id}/members`
- `guilds/{guild.id}/members/@me`
- `guilds/{guild.id}/members/{user.id}`
- `guilds/{guild.id}/members/@me/nick`
- `guilds/{guild.id}/members/search`
- `guilds/{guild.id}/members/{user.id}/roles/{role.id}`
- `guilds/{guild.id}/bans`
- `guilds/{guild.id}/bans/{user.id}`
- `guilds/{guild.id}/roles`
- `guilds/{guild.id}/roles/{role.id}`
- `guilds/{guild.id}/prune`
- `guilds/{guild.id}/regions`
- `guilds/{guild.id}/invites`
- `guilds/{guild.id}/integrations`
- `guilds/{guild.id}/integrations/{integration.id}`
- `guilds/{guild.id}/widget`
- `guilds/{guild.id}/widget.json`
- `guilds/{guild.id}/widget.png`
- `guilds/{guild.id}/audit-logs`
- `guilds/{guild.id}/vanity-url`
- `guilds/{guild.id}/welcome-screen`
- `guilds/{guild.id}/voice-states/@me`
- `guilds/{guild.id}/voice-states/{user.id}`
- `guilds/{guild.id}/scheduled-events`
- `guilds/{guild.id}/scheduled-events/{guild_scheduled_event.id}`
- `guilds/{guild.id}/scheduled-events/{guild_scheduled_event.id}/users`
- `guilds/templates/{template.code}`
- `guilds/{guild.id}/templates`
- `guilds/{guild.id}/templates/{template.code}`
- `guilds/{guild.id}/stickers`
- `guilds/{guild.id}/stickers/{sticker.id}`

<br>

Invite
- `invites/{invite.code}`

<br>

Stage Instance
- `stage-instances`
- `stage-instances/{channel.id}`

<br>

Sticker
- `stickers/{sticker.id}`
- `sticker-packs`

<br>

User
- `users/@me`
- `users/@me/guilds`
- `users/@me/guilds/{guild.id}`
- `users/@me/guilds/{guild.id}/member`
- `users/@me/channels`
- `users/@me/connections`
- `users/{user.id}`

<br>

Voice
- `voice/regions`

<br>

Webhook
- `webhooks/{webhook.id}`
- `webhooks/{webhook.id}/{webhook.token}`
- `webhooks/{webhook.id}/{webhook.token}/slack`
- `webhooks/{webhook.id}/{webhook.token}/github`
- `webhooks/{webhook.id}/{webhook.token}/messages/{message.id}`

<br>

Status
- `summary.json`
- `status.json`
- `components.json`
- `incidents.json`
- `incidents/unresolved.json`
- `scheduled-maintenances.json`
- `scheduled-maintenances/active.json`
- `scheduled-maintenances/upcoming.json`
