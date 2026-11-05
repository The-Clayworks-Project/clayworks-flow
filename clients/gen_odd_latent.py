import sys; sys.argv=['x']
exec(open('gen_status.py').read().split('# ---------------- PRIME')[0])
O=[(U,"Not in md"),(D,"13 Aug GTM Strategy call (Fireflies 01KZ881...)"),(U,"Not in md"),(D,"13 Aug GTM Strategy: 3-month pilot, no onboarding fee"),(U,"ROI in Hub (292%, 29 Oct); no ROI call"),
(U,"18 Aug Next Steps: proposal follow-up"),(D,"18 Aug Next Steps call"),(U,"Retainer amount not stated; target 8/month, CONFLICT: Callum says no guarantee"),(U,"No rules; qualified set by meeting outcome"),(X,"Not needed"),
(D,"Signed 26 Aug on Agree.com"),(D,"Tenant de711083"),(U,"Onboarding calls 18 Sep, 24 Sep; form not mentioned"),(D,"WhatsApp group Odd Latent x Clayworks; Drive folder Clayworks/Odd Latent"),
(D,"All client calls in Fireflies from 13 Aug; knowledge base v3"),(D,"SmartLead, Prosp, Client Hub, Blitz, Pronto, LeadsForge"),(U,"Prosp voice cloning broken until v2"),(D,"12 domains, 24 mailboxes pitched; warm-up since late Aug"),
(D,"18 Sep onboarding call (pivot)"),(D,"Catch-ups 1 Oct, 15 Oct, 29 Oct; next 12 Nov; cadence 14 days"),(U,"Signals used (charts, hiring, competitor followers); no tracking tool named"),
(D,"Campaign Plan v3, 21 Sep"),(D,"Apple charts, vendor lists"),(D,"Up to 3 titles per studio"),(D,"Big studio ABM from 1 Oct"),(D,"Dedupe by person rule; chart re-check"),(D,"Copy rules section 9"),(D,"Theo review 22 to 23 Sep"),
(D,"24 Sep: offer numbers cleared by client"),(D,"Buckets built in SmartLead"),(U,"Mailbox conflicts B5/B5b open"),(D,"Launch 24 to 25 Sep"),(U,"Not in md"),(U,"Agnes calls; only 174 calls all time"),(D,"BDR onboarding 28 Sep"),
(U,"Not in md"),(U,"Hyper Canny missed since 23 Oct"),(D,"16 meetings in Hub; 6 stale scheduled"),(U,"B4 bounce/block ~4.9%"),(D,"14-day client calls"),(D,"Bucket 4b, Asia test, PGC London"),(D,"B2 and B4 reviews"),
(D,"Invoices 1 to 3; invoice 3 due 14 Nov"),(D,"Health 77 green"),(D,"Month 2: 9 to 10 vs 8"),(X,"Not needed"),(X,"Not needed"),(U,"Pilot ends 9 Dec; renewal date unclear (9th vs 14th)"),
(X,"Active client"),(X,"Active client"),(X,"Active client"),(X,"Active client"),(X,"Active client")]
OC=[(D,"Tenant de711083"),(D,"[Client Hub list_tenant_owners not run] md: Callum and Theo own account"),(U,"Not in md"),(U,"Not in md"),(U,"No written rules"),
(D,"Blacklist 10 entries (5 existing customer, 5 do-not-contact); 27 Sep sweep 9 applied"),(D,"4 Nov sweep: no blacklisted company in any live or draft SmartLead campaign or the Prosp list"),
(D,"WhatsApp group"),(D,"Clayworks/Odd Latent folder"),(D,"Calls from 13 Aug"),(D,"Knowledge base v3, CLAUDE.md"),(D,"Pitch: 12 domains, 24 mailboxes"),(D,"DMARC p=reject, warm-up since late Aug"),(U,"Not in md"),
(D,"Mailboxes on campaigns"),(D,"LinkedIn live 14 Oct (late; Joy: my miss)"),(U,"Not in md"),(U,"No CloudTalk or CRM sync named"),(U,"Books into Tatu's calendar; no fixed link named"),(U,"Not in md"),(U,"Not in md"),
(D,"18 Sep onboarding; Tatu named data sources"),(D,"14-day calls"),(D,"Campaign Plan v3"),(U,"27 Sep sweep came after launch 24 to 25 Sep"),(D,"24 Sep: client cleared offer numbers"),(D,"Theo review"),(D,"Agnes 28 Sep"),
(D,"Live 24 to 25 Sep"),(D,"Signed 26 Aug, first send 24 Sep = 29 days (contract start was 9 Sep)")]
mk("odd-latent",O,OC,{"name":"Odd Latent","tenant":"de711083-fcf3-4ef9-8adf-8d0fe56988ca","state":"active pilot, health 77 green, ends 9 Dec 2026","raw_date":"v3, 4 Nov 2026"})
