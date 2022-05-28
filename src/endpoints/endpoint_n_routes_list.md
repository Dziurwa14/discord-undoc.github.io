# Endpoints & Routes

## Base URLs

**Base API URL** - `https://canary.discord.com/api/v9/`\
**Base Status API URL** - `https://discordstatus.com/api/v2/` or `https://discordstatus.com/`

## Endpoints

- `/activities`
- `/activities/applications/{application.id}/{guild.id}/{channel.id}/join-ticket`
- `/activities/guilds/{guild.id}/config`
- `/activities/guilds/{guild.id}/enable-wtp`
- `/activities/guilds/{guild.id}/shelf`
- `/activities/guilds/{guild.id}/{channel.id}/{application.id}`
- `/activities/statistics/applications/{application.id}`
- `/application-directory/applications`
- `/application-directory/applications/recommended`
- `/application-directory/applications/{application.id}`
- `/application-directory/applications/{application.id}/similar`
- `/application-directory/categories`
- `/applications`
- `/applications/detectable`
- `/applications/public`
- `/applications/trending/global`
- `/applications/{application.id}/achievements`
- `/applications/{application.id}/achievements/{achievement.id}`
- `/applications/{application.id}/app-icons/{hash}.png`
- `/applications/{application.id}/branches`
- `/applications/{application.id}/branches/{unknown}/builds/live`
- `/applications/{application.id}/branches/{unknown}/builds/{unknown}/size`
- `/applications/{application.id}/branches/{unknown}/storage`
- `/applications/{application.id}/commands`
- `/applications/{application.id}/commands/{command.id}`
- `/applications/{application.id}/entitlements`
- `/applications/{application.id}/entitlements/{entitlement.id}`
- `/applications/{application.id}/entitlements/{entitlement.id}/consume`
- `/applications/{application.id}/external-assets`
- `/applications/{application.id}/guilds/{guild.id}/commands`
- `/applications/{application.id}/guilds/{guild.id}/commands/permissions`
- `/applications/{application.id}/guilds/{guild.id}/commands/{command.id}`
- `/applications/{application.id}/guilds/{guild.id}/commands/{command.id}/permissions`
- `/applications/{application.id}/payment-payout-groups`
- `/applications/{application.id}/public`
- `/applications/{application.id}/skus`
- `/auth/authorize-ip`
- `/auth/forgot`
- `/auth/handoff`
- `/auth/handoff/exchange`
- `/auth/location-metadata`
- `/auth/login`
- `/auth/logout`
- `/auth/mfa/sms`
- `/auth/mfa/sms/send`
- `/auth/mfa/totp`
- `/auth/register`
- `/auth/register/phone`
- `/auth/reset`
- `/auth/verify`
- `/auth/verify/resend`
- `/auth/verify/view-backup-codes-challenge`
- `/billing/apple/apply-receipt`
- `/billing/popup-bridge/{unknown}`
- `/billing/popup-bridge/{unknown}/callback`
- `/billing/popup-bridge/{unknown}/callback/{unknown}/{unknown}`
- `/billing/verify-purchase-request`
- `/branches`
- `/channels`
- `/channels/{channel.id}`
- `/channels/{channel.id}/application-commands/search`
- `/channels/{channel.id}/call`
- `/channels/{channel.id}/call/ring`
- `/channels/{channel.id}/call/stop-ringing`
- `/channels/{channel.id}/convert`
- `/channels/{channel.id}/directory-entries`
- `/channels/{channel.id}/directory-entries/counts`
- `/channels/{channel.id}/directory-entries/list`
- `/channels/{channel.id}/directory-entries/search`
- `/channels/{channel.id}/directory-entry/{unknown}`
- `/channels/{channel.id}/follower-message-stats`
- `/channels/{channel.id}/follower-stats`
- `/channels/{channel.id}/followers`
- `/channels/{channel.id}/greet`
- `/channels/{channel.id}/icons/{hash}.jpg`
- `/channels/{channel.id}/invites`
- `/channels/{channel.id}/messages`
- `/channels/{channel.id}/messages/ack`
- `/channels/{channel.id}/messages/bulk-delete`
- `/channels/{channel.id}/messages/search`
- `/channels/{channel.id}/messages/{message.id}`
- `/channels/{channel.id}/messages/{message.id}/crosspost`
- `/channels/{channel.id}/messages/{message.id}/reactions`
- `/channels/{channel.id}/messages/{message.id}/reactions/{emoji}`
- `/channels/{channel.id}/messages/{message.id}/reactions/{emoji}/@me`
- `/channels/{channel.id}/messages/{message.id}/reactions/{emoji}/{user.id}`
- `/channels/{channel.id}/messages/{message.id}/threads`
- `/channels/{channel.id}/messages/{message.id}/ack`
- `/channels/{channel.id}/messages/{message.id}/hide-guild-feed`
- `/channels/{channel.id}/messages/{message.id}/interaction-data`
- `/channels/{channel.id}/permissions`
- `/channels/{channel.id}/permissions/{overwrite.id}`
- `/channels/{channel.id}/pins`
- `/channels/{channel.id}/pins/ack`
- `/channels/{channel.id}/pins/{message.id}`
- `/channels/{channel.id}/post-data`
- `/channels/{channel.id}/recipients`
- `/channels/{channel.id}/recipients/{user.id}`
- `/channels/{channel.id}/store-listing`
- `/channels/{channel.id}/store-listing/entitlement-grant`
- `/channels/{channel.id}/store-listings/{unknown}`
- `/channels/{channel.id}/tags`
- `/channels/{channel.id}/tags/{unknown}`
- `/channels/{channel.id}/thread-members`
- `/channels/{channel.id}/thread-members/@me`
- `/channels/{channel.id}/thread-members/@me/settings`
- `/channels/{channel.id}/thread-members/{user.id}`
- `/channels/{channel.id}/threads`
- `/channels/{channel.id}/threads/active`
- `/channels/{channel.id}/threads/archived/private`
- `/channels/{channel.id}/threads/archived/public`
- `/channels/{channel.id}/threads/archived/{unknown}`
- `/channels/{channel.id}/threads/search`
- `/channels/{channel.id}/typing`
- `/channels/{channel.id}/users/@me/threads/archived/private`
- `/channels/{channel.id}/webhooks`
- `/connections/{unknown}/authorize`
- `/connections/{unknown}/authorize?continuation=true`
- `/connections/{unknown}/callback`
- `/connections/{unknown}/callback-continuation/{unknown}`
- `/debug-logs/multi/{unknown}`
- `/debug-logs/{unknown}/{unknown}`
- `/discoverable-guilds`
- `/discovery/categories`
- `/discovery/valid-term`
- `/discovery/{unknown}`
- `/emojis/{unknown}.{unknown}`
- `/emojis/{unknown}/guild`
- `/entitlements/gift-codes/{unknown}`
- `/entitlements/gift-codes/{unknown}/redeem`
- `/experiments`
- `/friend-suggestions`
- `/friend-suggestions/{unknown}`
- `/gateway`
- `/gateway/bot`
- `/gifs/search`
- `/gifs/select`
- `/gifs/suggest`
- `/gifs/trending`
- `/gifs/trending-gifs`
- `/gifs/trending-search`
- `/google-play/downgrade-subscription`
- `/google-play/verify-purchase-token`
- `/guild-events`
- `/guild-events/{unknown}/images/{unknown}.{unknown}`
- `/guild-recommendations`
- `/guilds`
- `/guilds/automations/email-domain-lookup`
- `/guilds/automations/email-domain-lookup/verify`
- `/guilds/automations/email-domain-lookup/verify-code`
- `/guilds/templates/{template.code}`
- `/guilds/{guild.id}`
- `/guilds/{guild.id}/ack/{unknown}/{unknown}`
- `/guilds/{guild.id}/active-channels`
- `/guilds/{guild.id}/analytics/engagement/overview`
- `/guilds/{guild.id}/analytics/growth-activation/overview`
- `/guilds/{guild.id}/analytics/growth-activation/retention`
- `/guilds/{guild.id}/analytics/member-insights`
- `/guilds/{guild.id}/analytics/overview`
- `/guilds/{guild.id}/application-commands/{unknown}`
- `/guilds/{guild.id}/applications`
- `/guilds/{guild.id}/audit-logs`
- `/guilds/{guild.id}/auto-moderation/rules`
- `/guilds/{guild.id}/auto-moderation/rules/{unknown}`
- `/guilds/{guild.id}/banners/{unknown}.{unknown}`
- `/guilds/{guild.id}/bans`
- `/guilds/{guild.id}/bans/{user.id}`
- `/guilds/{guild.id}/channels`
- `/guilds/{guild.id}/creator-monetization/enable-requests`
- `/guilds/{guild.id}/creator-monetization/enable-requests/{unknown}/accept-terms`
- `/guilds/{guild.id}/creator-monetization/requirements`
- `/guilds/{guild.id}/delete`
- `/guilds/{guild.id}/directory-entries/broadcast`
- `/guilds/{guild.id}/discovery-categories/{unknown}`
- `/guilds/{guild.id}/discovery-checklist`
- `/guilds/{guild.id}/discovery-metadata`
- `/guilds/{guild.id}/discovery-requirements`
- `/guilds/{guild.id}/discovery-splashes/{unknown}.jpg`
- `/guilds/{guild.id}/emojis`
- `/guilds/{guild.id}/emojis/{emoji.id}`
- `/guilds/{guild.id}/guild-feed`
- `/guilds/{guild.id}/guild-feed/feature`
- `/guilds/{guild.id}/guild-feed/mark-seen`
- `/guilds/{guild.id}/guild-feed/preference`
- `/guilds/{guild.id}/icons/{unknown}.{unknown}`
- `/guilds/{guild.id}/integrations`
- `/guilds/{guild.id}/integrations/{integration.id}`
- `/guilds/{guild.id}/integrations/{unknown}/sync`
- `/guilds/{guild.id}/invites`
- `/guilds/{guild.id}/member-verification`
- `/guilds/{guild.id}/members`
- `/guilds/{guild.id}/members/@me`
- `/guilds/{guild.id}/members/@me/nick`
- `/guilds/{guild.id}/members/search`
- `/guilds/{guild.id}/members/{unknown}/nick`
- `/guilds/{guild.id}/members/{user.id}`
- `/guilds/{guild.id}/members/{user.id}/roles/{role.id}`
- `/guilds/{guild.id}/messages/search`
- `/guilds/{guild.id}/mfa`
- `/guilds/{guild.id}/premium/subscriptions`
- `/guilds/{guild.id}/premium/subscriptions/{unknown}`
- `/guilds/{guild.id}/preview`
- `/guilds/{guild.id}/prune`
- `/guilds/{guild.id}/regions`
- `/guilds/{guild.id}/requests`
- `/guilds/{guild.id}/requests/@me`
- `/guilds/{guild.id}/requests/{unknown}`
- `/guilds/{guild.id}/requests/{unknown}/ack`
- `/guilds/{guild.id}/role-prompts`
- `/guilds/{guild.id}/role-prompts/{unknown}`
- `/guilds/{guild.id}/role-subscriptions/group-listings/{unknown}`
- `/guilds/{guild.id}/role-subscriptions/group-listings/{unknown}/subscription-listings/{unknown}`
- `/guilds/{guild.id}/role-subscriptions/settings`
- `/guilds/{guild.id}/role-subscriptions/subscription-listings/{unknown}/trial`
- `/guilds/{guild.id}/role-subscriptions/subscription-listings/{unknown}/trial/{unknown}/eligibility`
- `/guilds/{guild.id}/role-subscriptions/trials`
- `/guilds/{guild.id}/role-subscriptions/trials/metrics-overview`
- `/guilds/{guild.id}/roles`
- `/guilds/{guild.id}/roles/member-counts`
- `/guilds/{guild.id}/roles/{role.id}`
- `/guilds/{guild.id}/roles/{unknown}/member-ids`
- `/guilds/{guild.id}/roles/{unknown}/members`
- `/guilds/{guild.id}/scheduled-events`
- `/guilds/{guild.id}/scheduled-events/{guild_scheduled_event.id}`
- `/guilds/{guild.id}/scheduled-events/{guild_scheduled_event.id}/users`
- `/guilds/{guild.id}/scheduled-events/{unknown}/users/@me`
- `/guilds/{guild.id}/soundboard-sounds`
- `/guilds/{guild.id}/soundboard-sounds/{unknown}`
- `/guilds/{guild.id}/splashes/{unknown}.jpg`
- `/guilds/{guild.id}/stickers`
- `/guilds/{guild.id}/stickers/{sticker.id}`
- `/guilds/{guild.id}/templates`
- `/guilds/{guild.id}/templates/{template.code}`
- `/guilds/{guild.id}/threads/active`
- `/guilds/{guild.id}/top-read-channels`
- `/guilds/{guild.id}/users/{unknown}/avatars/{unknown}.{unknown}`
- `/guilds/{guild.id}/users/{unknown}/banners/{unknown}.{unknown}`
- `/guilds/{guild.id}/vanity-url`
- `/guilds/{guild.id}/voice-states/@me`
- `/guilds/{guild.id}/voice-states/{user.id}`
- `/guilds/{guild.id}/webhooks`
- `/guilds/{guild.id}/welcome-screen`
- `/guilds/{guild.id}/widget`
- `/guilds/{guild.id}/widget.json`
- `/guilds/{guild.id}/widget.png`
- `/hub-waitlist/signup`
- `/hypesquad/online`
- `/integrations`
- `/integrations/{unknown}/join`
- `/integrations/{unknown}/search`
- `/interactions`
- `/interactions/{interaction.id}/{interaction.token}/callback`
- `/invites/{invite.code}`
- `/lobbies`
- `/lobbies/search`
- `/lobbies/{lobby.id}`
- `/lobbies/{lobby.id}/members/{user.id}`
- `/lobbies/{lobby.id}/send`
- `/metrics`
- `/networking/token`
- `/oauth2/@me`
- `/oauth2/allowlist/accept`
- `/oauth2/applications/@me`
- `/oauth2/applications/{unknown}/assets`
- `/oauth2/applications/{unknown}/rpc`
- `/oauth2/authorize`
- `/oauth2/authorize/webhook-channels`
- `/oauth2/tokens`
- `/oauth2/tokens/{unknown}`
- `/outbound-promotions`
- `/outbound-promotions/preview`
- `/outbound-promotions/{unknown}/claim`
- `/partners/apply`
- `/partners/connections`
- `/partners/{unknown}/requirements`
- `/phone-verifications/resend`
- `/phone-verifications/validate-support-ticket`
- `/phone-verifications/verify`
- `/private/bug-reports`
- `/promotions/funimation`
- `/read-states/ack-bulk`
- `/report`
- `/report/options`
- `/reporting/menu/{unknown}`
- `/reporting/{unknown}`
- `/reports`
- `/reports/channels/{unknown}/messages/{unknown}`
- `/roles/{unknown}/icons/{unknown}.png`
- `/science`
- `/soundboard-sounds/{unknown}`
- `/sso`
- `/stage-instances`
- `/stage-instances/extra`
- `/stage-instances/{channel.id}`
- `/sticker-packs`
- `/sticker-packs/directory-v2/{unknown}`
- `/sticker-packs/{unknown}`
- `/stickers/{sticker.id}`
- `/stickers/{unknown}.{unknown}`
- `/stickers/{unknown}/guild`
- `/store/applications/{unknown}/assets/{unknown}.{unknown}`
- `/store/directory-layouts/{unknown}`
- `/store/directory/{unknown}`
- `/store/eulas/{unknown}`
- `/store/listings/{unknown}`
- `/store/price-tiers`
- `/store/published-listings/applications`
- `/store/published-listings/applications/{unknown}`
- `/store/published-listings/skus`
- `/store/published-listings/skus/{unknown}`
- `/store/published-listings/skus/{unknown}/guild/join`
- `/store/published-listings/skus/{unknown}/subscription-plans`
- `/store/skus/{sku.id}/discounts/{user.id}`
- `/store/skus/{unknown}`
- `/store/skus/{unknown}/listings`
- `/store/skus/{unknown}/purchase`
- `/streams/{unknown}/notify`
- `/streams/{unknown}/preview`
- `/streams/{unknown}/stream`
- `/subscription-plans/{unknown}/guild-role-subscription-group-listing`
- `/teams`
- `/templates/{unknown}/icons/{unknown}.{unknown}`
- `/tenor`
- `/tutorial/indicators`
- `/tutorial/indicators/suppress`
- `/tutorial/indicators/{unknown}`
- `/unverified-applications`
- `/unverified-applications/icons`
- `/users`
- `/users/@me`
- `/users/@me/activities/statistics/applications`
- `/users/@me/affinities/guilds`
- `/users/@me/affinities/users`
- `/users/@me/agreements`
- `/users/@me/applications/{application.id}/achievements`
- `/users/@me/applications/{unknown}/entitlement-ticket`
- `/users/@me/applications/{unknown}/entitlements`
- `/users/@me/applications/{unknown}/ticket`
- `/users/@me/billing/country-code`
- `/users/@me/billing/payment-sources`
- `/users/@me/billing/payment-sources/validate-billing-address`
- `/users/@me/billing/payment-sources/{unknown}`
- `/users/@me/billing/payments`
- `/users/@me/billing/payments/{unknown}`
- `/users/@me/billing/payments/{unknown}/refund`
- `/users/@me/billing/payments/{unknown}/void`
- `/users/@me/billing/paypal/billing-agreement-tokens`
- `/users/@me/billing/stripe/payment-intents/payments/{unknown}`
- `/users/@me/billing/stripe/payment-intents/{unknown}`
- `/users/@me/billing/stripe/setup-intents`
- `/users/@me/billing/subscriptions`
- `/users/@me/billing/subscriptions/preview`
- `/users/@me/billing/subscriptions/{unknown}`
- `/users/@me/billing/subscriptions/{unknown}/invoices`
- `/users/@me/billing/subscriptions/{unknown}/invoices/{unknown}/pay`
- `/users/@me/billing/subscriptions/{unknown}/preview`
- `/users/@me/billing/user-trial-offer`
- `/users/@me/billing/user-trial-offer/{unknown}/ack`
- `/users/@me/captcha/verify`
- `/users/@me/channels`
- `/users/@me/connections`
- `/users/@me/connections/contacts/@me/external-friend-list-entries`
- `/users/@me/connections/contacts/@me/external-friend-list-entries/settings`
- `/users/@me/connections/{unknown}/{unknown}`
- `/users/@me/connections/{unknown}/{unknown}/access-token`
- `/users/@me/consent`
- `/users/@me/delete`
- `/users/@me/devices`
- `/users/@me/disable`
- `/users/@me/email`
- `/users/@me/email-settings`
- `/users/@me/email/verify-code`
- `/users/@me/entitlements/gift-codes`
- `/users/@me/entitlements/gift-codes/{unknown}`
- `/users/@me/entitlements/gifts`
- `/users/@me/guilds`
- `/users/@me/guilds/premium/subscription-slots`
- `/users/@me/guilds/premium/subscription-slots/{unknown}/cancel`
- `/users/@me/guilds/premium/subscription-slots/{unknown}/uncancel`
- `/users/@me/guilds/premium/subscriptions`
- `/users/@me/guilds/premium/subscriptions/cooldown`
- `/users/@me/guilds/{guild.id}`
- `/users/@me/guilds/{guild.id}/member`
- `/users/@me/guilds/{unknown}/settings`
- `/users/@me/harvest`
- `/users/@me/invites`
- `/users/@me/join-request-guilds`
- `/users/@me/library`
- `/users/@me/library/{unknown}`
- `/users/@me/library/{unknown}/{unknown}`
- `/users/@me/library/{unknown}/{unknown}/installed`
- `/users/@me/mentions`
- `/users/@me/mentions/{unknown}`
- `/users/@me/mfa/codes-verification`
- `/users/@me/mfa/sms/disable`
- `/users/@me/mfa/sms/enable`
- `/users/@me/mfa/totp/disable`
- `/users/@me/mfa/totp/enable`
- `/users/@me/notes`
- `/users/@me/notes/{unknown}`
- `/users/@me/outbound-promotions/codes`
- `/users/@me/phone`
- `/users/@me/phone/verify`
- `/users/@me/premium-usage`
- `/users/@me/relationships/bulk`
- `/users/@me/relationships/{unknown}`
- `/users/@me/remote-auth`
- `/users/@me/remote-auth/cancel`
- `/users/@me/remote-auth/finish`
- `/users/@me/scheduled-events`
- `/users/@me/settings`
- `/users/@me/settings-proto/{unknown}`
- `/users/@me/settings/game-notifications`
- `/users/@me/settings/game-notifications/overrides`
- `/users/@me/sticker-packs`
- `/users/@me/survey`
- `/users/@me/video-filters/assets`
- `/users/@me/video-filters/assets/{unknown}`
- `/users/@me/video-filters/assets/{unknown}/last-used`
- `/users/disable-email-notifications`
- `/users/{user.id}`
- `/users/{user.id}/applications/{unknown}/achievements/{unknown}`
- `/users/{user.id}/avatar-decorations/{unknown}.{unknown}`
- `/users/{user.id}/avatars/{unknown}.{unknown}`
- `/users/{user.id}/banners/{unknown}.{unknown}`
- `/users/{user.id}/profile`
- `/users/{user.id}/relationships`
- `/users/{user.id}/sessions/{unknown}/activities/{unknown}/1`
- `/users/{user.id}/sessions/{unknown}/activities/{unknown}/metadata`
- `/users/{user.id}/video-filter-assets/{unknown}/{unknown}.{unknown}`
- `/voice/regions`
- `/webhooks/{application.id}/{interaction.token}`
- `/webhooks/{application.id}/{interaction.token}/messages/@original`
- `/webhooks/{application.id}/{interaction.token}/messages/{message.id}`
- `/webhooks/{webhook.id}`
- `/webhooks/{webhook.id}/{webhook.token}`
- `/webhooks/{webhook.id}/{webhook.token}/github`
- `/webhooks/{webhook.id}/{webhook.token}/messages/{message.id}`
- `/webhooks/{webhook.id}/{webhook.token}/slack`

## Routes

- `/activity`
- `/app`
- `/application-directory/{unknown}`
- `/apps`
- `/authorize-ip`
- `/authorize-payment`
- `/billing`
- `/billing/guild-subscriptions/purchase`
- `/billing/login/handoff`
- `/billing/payment-sources/create`
- `/billing/payments`
- `/billing/popup-bridge/callback`
- `/billing/premium/manage`
- `/billing/premium/subscribe`
- `/billing/premium/switch-plan`
- `/billing/promotions/{unknown}`
- `/channels/@me`
- `/channels/{unknown}/{unknown}/{unknown}`
- `/connect/authorize`
- `/connections/xbox/intro`
- `/connections/xbox/pin`
- `/connections/{unknown}`
- `/disable-email-notifications`
- `/domain-migration`
- `/download-qr-code`
- `/events/{unknown}/{unknown}`
- `/feature/{unknown}`
- `/gifts/{unknown}`
- `/gifts/{unknown}/login`
- `/guild-discovery`
- `/guild-stages/{unknown}/{unknown}`
- `/guilds/create`
- `/guilds/{unknown}/premium-guild-subscriptions`
- `/guilds/{unknown}/requests/{unknown}`
- `/handoff`
- `/invite-proxy/{unknown}`
- `/invite/{unknown}`
- `/invite/{unknown}/login`
- `/invite/{unknown}/register`
- `/library`
- `/library/inventory`
- `/library/settings`
- `/library/{unknown}/{unknown}`
- `/login`
- `/login/handoff`
- `/member-verification-for-hub/{unknown}/{unknown}`
- `/member-verification/{unknown}/{unknown}`
- `/mweb-handoff`
- `/oauth2/allowlist/accept`
- `/oauth2/authorize`
- `/oauth2/authorized`
- `/oauth2/error`
- `/open-app-from-email`
- `/popout`
- `/register`
- `/reset`
- `/settings/changelogs/{unknown}`
- `/settings/{unknown}/{unknown}`
- `/store`
- `/store/applications/{unknown}/{unknown}`
- `/store/skus/{unknown}/{unknown}`
- `/template/{unknown}`
- `/template/{unknown}/login`
- `/users/{unknown}`
- `/verify`
- `/verify-hub-email`
- `/verify-request`
- `/voice/{unknown}/{unknown}/{unknown}`
- `/welcome/{unknown}/{unknown}`

## Status API

- `components.json`
- `incidents.json`
- `incidents/unresolved.json`
- `metrics-display/5k2rt9f7pmny/day.json`
- `metrics-display/5k2rt9f7pmny/month.json`
- `metrics-display/5k2rt9f7pmny/week.json`
- `scheduled-maintenances.json`
- `scheduled-maintenances/active.json`
- `scheduled-maintenances/upcoming.json`
- `status.json`
- `summary.json`