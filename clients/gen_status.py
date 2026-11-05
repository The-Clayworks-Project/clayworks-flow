import json,re
STEPS="""Log the first meeting|Intro call|Free sample: 25 accounts with signals|GTM strategy call|ROI call and calculator|Proposal page|Proposal deep dive|Set price and meeting promise|Agree 3 rules for a 'qualified' meeting|Consulting first (if needed)|Contract review and signing|Create the client's Hub space|Fill in the onboarding form|Group chat and shared folder|Record every call and make a context file|Connect the tools|Easy to forget setup items|Order sending inboxes early|Kickoff call|Book weekly catch-ups|Turn on signal tracking|Client profile and campaign plan|Find the right companies|Find the right people|Map who to contact at signal accounts|Check the list|Write the messages|Check the messages|Client approves the messages|Build the campaign as a draft|Final check before launch|Joy launches|Move the plan to live|Phone list for the callers|Callers get ready|Slack alerts for replies and meetings|Sort replies every day|Book and check meetings|Keep inboxes healthy|Weekly client catch-up|New campaign ideas|Close out finished campaigns|Monthly review and invoice|Health score and at-risk flag|Meetings vs promise|Save plan|Extend if the target is missed|Renewal check|Notice and owner|Hand over data|Stop sending|Cancel inboxes, then domains|Close accounts and sign off""".split("|")
CHECK="""Hub tenant and CSM account created|Owners set in Hub|Onboarding form sent|Form complete (all 8 sections)|3 qualified meeting rules written|Blacklist collected and loaded|Blacklist sanity check|Group chat created|Drive folder shared|Fireflies on client calls|Client folder, context file, Helper bot|Warm inboxes checked, purchase approved|Domains and inboxes bought, DNS passes, warm-up on|InboxKit forwarding address checked|Smartlead connected and tagged|Prosp connected and LinkedIn profiles live|Prosp webhook set|CloudTalk numbers and CRM sync|Calendar and fixed meeting link per caller|Slack alert channels on|White Whale signals on|Kickoff call held, data asks listed|Weekly catch-ups booked|Profile and campaign plan|Blacklist gate passed on first lists|Copy approved|Draft built, pre-launch QA passed|BDRs onboarded|Launch and plan stage live|Time to first send recorded""".split("|")
D,N,U,X="done","not_done","unclear","n_a"
def mk(slug,steps,checks,meta):
    assert len(steps)==53 and len(checks)==30,(slug,len(steps),len(checks))
    out={"client":meta,"status_values":"done | not_done | unclear | n_a","source_default":f"clients/raw/{slug}.md","steps":{},"checklist":{}}
    for i,(s,e) in enumerate(steps):
        out["steps"][f"step{i}"]={"title":STEPS[i],"status":s,"evidence":e,"source":"md" if not e.startswith("[") else e.split("]")[0][1:]}
    for i,(s,e) in enumerate(checks):
        out["checklist"][f"c{i+1}"]={"title":CHECK[i],"status":s,"evidence":e,"source":"md"}
    for k in ("steps","checklist"):
        c={}
        for v in out[k].values(): c[v["status"]]=c.get(v["status"],0)+1
        out[k+"_counts"]=c
    txt=json.dumps(out,indent=1,ensure_ascii=False)
    assert "\u2014" not in txt and "\u2013" not in txt
    open(f"/workspace/clayworks/client-flow/clients/{slug}.status.json","w").write(txt)
    print(slug,out["steps_counts"],out["checklist_counts"])
    return out

# ---------------- PRIME ----------------
P=[(U,"No record of first meeting"),(U,"No intro call record; Fireflies only from 24 Jun"),(U,"Not mentioned"),(U,"Not mentioned"),(U,"Not mentioned"),
(D,"\"Lovable proposal, 'Prime Marketing Growth Engine' (project b1d325c8...)\""),(U,"Not mentioned"),
(D,"\"About EUR 2,500/month... promised 5 meetings a month\""),(U,"No written definition found; 'qualified' used on meetings only"),(X,"Not mentioned"),
(D,"\"22 Apr: contract signed through Agree.com\" (contract/SOW never found)"),
(D,"\"22 Apr... Client Hub tenant created\" 4895873f"),(D,"\"23 Apr: onboarding form completed\" (answers never found)"),
(D,"\"Shared channel #prime-marketing C0AU28JRZBR\"; Drive folder 1GGIgNE0..."),(N,"\"Fireflies only goes back to 24 Jun, so there's no recording\" of kickoff; no context file named"),
(D,"InboxKit, SmartLead, Prosp (1 to 11 May), CloudTalk all used"),(U,"Not mentioned"),(D,"\"9 domains and 18 mailboxes bought in InboxKit the same day\" (23 Apr)"),
(D,"\"30 Apr: kickoff call\" (not recorded, notes never found)"),(D,"\"26 Jun weekly call\", \"21 Sep weekly\""),(U,"Hiring signals used in campaigns; no signal tool named"),
(N,"\"There was never a formal ICP document\""),(D,"Blitz/Pronto/LeadsForge lists, competitor-agency followers"),(D,"Enriched decision makers (Blitz/Pronto/LeadsForge)"),
(U,"Hiring-signal campaigns in May; no account mapping described"),(D,"\"11 to 13 Oct... 576 companies (621 contacts) were usable after a full QA\" (Oct only)"),
(D,"Scripts v1 to v7, gap report offer"),(U,"Not mentioned"),(U,"Not mentioned"),(D,"SmartLead and Prosp campaigns built"),(U,"Not mentioned"),
(D,"\"6 May: campaigns went live\" (who launched not stated)"),(U,"Plan 490558c0 for SmartLead 4124101 only"),(D,"\"Agnes made about 240 calls to Dutch numbers\""),
(U,"Not mentioned"),(D,"\"Prosp reply bot posts to #prosp-linkedin C09BNN7EMHU\""),
(U,"Not mentioned"),(D,"About 10 meetings booked, 4 of 9 did not happen"),(U,"\"primeadresults.com hit a SURBL blocklist\"; 8.3% bounce on one mailbox; no routine named"),
(D,"Weekly calls 26 Jun, 21 Sep; renewal sync 23 Jul"),(D,"V2 Paid Audit Hook, gap report, competitor followers"),(D,"\"Theo closed out the September campaign (card 1e295c0e)\""),
(U,"\"asked for a monthly check-in\"; tracker \"filled for May only\""),
(U,"No health score in md"),(D,"\"Only 2 meetings against 5 a month promised; 13 meetings were owed\""),(D,"\"contract moved to 30-day rolling\"; \"keep going for two months\""),
(D,"\"13 meetings were owed and rolled over\""),(D,"\"23 Jul renewal sync\""),
(D,"\"14 Oct... offboarding at end of October was treated as settled\"; notice terms disputed 23 Oct"),(U,"\"export data only if the client asks\"; no ask recorded"),
(D,"\"SmartLead 4124101 paused 22 Oct\"; Prosp campaigns stopped"),(U,"Mailboxes cancelled 21 to 22 Oct; domains only \"scheduled for deletion\""),
(N,"\"Client Hub tenant: Still active\"; Prosp \"Account cancellation not confirmed\"; ops card bc8643d1 open")]
PC=[(D,"Tenant 4895873f created 22 Apr"),(D,"Theo owner, Joy from 6 Oct"),(D,"Implied by form completed 23 Apr"),(U,"\"onboarding form completed\" but answers \"never found anywhere\""),
(U,"No written rules found"),(N,"\"Prime's promised exclusion CSV\" never found; only Econocom, Skalar named plus 18 opt-outs on Hub blacklist"),(U,"Not mentioned"),
(D,"#prime-marketing"),(D,"Drive folder 1GGIgNE0mxPWBoSRgfwSkxDbb-J3e2ZQA"),(U,"Fireflies from 24 Jun only; later calls recorded"),
(U,"Handover brief 6 Oct only; no context file or Helper named"),(D,"Bought 23 Apr"),(D,"\"first payment covered 2 weeks of warm-up\""),(U,"Not mentioned"),
(U,"InboxKit tag 6f3fa685; SmartLead tagging not mentioned"),(D,"\"1 to 11 May: Prosp set up\", voice clone"),(D,"Reply bot posts to #prosp-linkedin"),
(U,"\"untagged in CloudTalk\"; no CRM sync"),(U,"Not mentioned"),(D,"#prosp-linkedin reply bot (LinkedIn only)"),(U,"Not mentioned"),
(D,"\"30 Apr: kickoff call\" (no notes)"),(D,"Weekly calls"),(N,"\"never a formal ICP document\""),
(U,"\"UK Competitor Campaign/ ... dedupe script and blacklist\" exists for Oct; nothing for May lists"),(U,"Not mentioned; guarantee wording drifted"),
(U,"Oct list QA only"),(D,"Callum Moon and Agnes Sacher booked and called"),(D,"Live 6 May"),(D,"Signed 22 Apr, live 6 May = 14 days (computed from md dates)")]
mk("prime-marketing",P,PC,{"name":"Prime Marketing","tenant":"4895873f-9a4b-485c-b29a-72e96370b99e","state":"churned 31 Oct 2026","raw_date":"compiled 4 Nov 2026"})

# ---------------- VARIOLYTICS ----------------
V=[(U,"Sales call recording missing; \"Fireflies starts 25 Jun\""),(U,"Not in md"),(U,"Not in md"),(U,"Not in md"),(U,"Hub has ACV 40k and close rate 0.4 \"for ROI maths\"; no ROI call found"),
(U,"Not in md"),(U,"Not in md"),(D,"\"15 meetings a month\" guarantee; fee unclear (one GBP 4,500 data point)"),(U,"\"Unknowns to chase: The qualified-meeting definition\""),(X,"Not in md"),
(D,"\"Outbound contract start 25 Feb 2026\" (signed copy missing)"),
(D,"\"Hub tenant created 11 Mar\""),(D,"Onboarding doc \"Plan of Action\" (a doc, not the form)"),(U,"Drive folder 6 Mar; \"Slack: no client channel\""),
(U,"Fireflies from 25 Jun; no context file named; Joy's handoff docs 27 Oct"),(D,"InboxKit, SmartLead, Prosp, CloudTalk; Pipedrive integration overdue"),(U,"Plaintext passwords in tracker sheet"),
(D,"\"Infrastructure, set up 1 Mar\": 9 domains, 18 mailboxes"),(U,"No kickoff in md"),(D,"\"catch-up every 14 days\"; Week 32 check-in"),(U,"Norway \"high-intent signals\" campaign; no tracking tool named"),
(D,"\"Plan of Action\": Nordic WWTPs, personas, >10,000 PE plus BNR"),(D,"BNR filter from EU E-PRTR register"),(D,"Blitz, Pronto, website scrapes"),(D,"\"Build accounts first, then people\""),
(D,"BNR filter; \"4 Nov: Blacklist check of all live SmartLead campaigns: clean\" apart from InfraServ"),(D,"Germany v2/v4, municipal v1"),(D,"\"Theo's copy review\" 27 to 28 Oct"),
(U,"No client copy approval in md"),(D,"\"Germany drafts built\" 27 to 28 Oct"),(D,"4 Nov blacklist check of live campaigns"),
(D,"Joy owns builds from week of 26 Oct; Europe built"),(D,"\"4 Nov: Hub plans set live\""),(D,"Phones from websites go on Hub cards; Agnes calls"),(D,"Agnes books by phone from June"),
(U,"\"bookings go to #all-clayworks\"; no client channel; no reply alert named"),
(U,"Not in md"),(D,"77 meeting records; 16 rescheduled with no outcome"),(N,"\"2 to 3 Nov, mailboxes RED\": 6.0% bounce, 3 rested, 0 spares"),
(D,"Check-ins every 14 days; next 12 Nov"),(D,"Germany split, Europe campaign, BNR filter"),(D,"\"Denmark closed out\" 4 Nov"),(D,"\"Invoicing moved to a 14-day cycle\""),
(D,"\"Account health is 43, red, At Risk since 27 Oct\""),(D,"\"About 12-13 meetings a month; guarantee is 15\""),(U,"No save plan in md; \"pump the numbers\" push"),(U,"Not in md"),
(N,"Outbound renews 31 Dec; ads pilot renews or ends 30 Nov; \"exact ads review date\" unknown"),
(X,"Active client"),(X,"Active client"),(X,"Active client"),(X,"Active client"),(X,"Active client")]
VC=[(D,"Tenant 009782d9 created 11 Mar"),(D,"\"Callum and Theo are the primary owners on the Hub\""),(U,"Onboarding doc exists; form not mentioned"),(D,"\"Plan of Action\" doc (form not mentioned)"),
(U,"\"qualified-meeting definition\" listed as unknown"),(D,"\"132 entries uploaded. It now has 167: 123 existing customers, 24 do-not-contact, 20 opt-outs\""),
(D,"\"4 Nov: Blacklist check of all live SmartLead campaigns: clean\"; BUT Waterschap Limburg booked 25 Nov and 4 blacklisted people may be in Prosp"),
(N,"\"Slack: no client channel\""),(D,"\"Drive folder created 6 Mar\""),(U,"\"Fireflies starts 25 Jun\""),(U,"\"14-page Account Handover Handbook\" missing; no Helper named"),
(D,"18 mailboxes from InboxKit"),(D,"Cloudflare domains set up 1 Mar"),(D,"\"forwarding to variolytics.com\""),(U,"Not in md"),
(D,"\"2 Prosp LinkedIn licences\"; Nick disconnected 28 and 30 Oct"),(U,"Not in md"),(N,"2 CloudTalk numbers, but \"No call metrics are logged\" and Pipedrive integration overdue since 19 Oct"),
(D,"\"Pipedrive scheduler on MS Teams\"; booking pages broke 6 Oct and 30 Oct"),(U,"Bookings to #all-clayworks"),(U,"Not in md"),(U,"No kickoff in md"),(D,"Every 14 days"),
(D,"Plan of Action"),(U,"No gate record for March lists; 4 Nov check on live campaigns only"),(U,"Theo internal review only"),(D,"Germany drafts plus Theo review"),
(D,"Callum Mar to May, Agnes from June"),(D,"First campaign 15 Mar; Hub plans live 4 Nov"),(D,"Contract 25 Feb, first send 15 Mar = 18 days (computed from md dates)")]
mk("variolytics",V,VC,{"name":"Variolytics","tenant":"009782d9-ce56-40ed-bd66-b7035ced02f7","state":"active, health 43 red At Risk","raw_date":"compiled 4 Nov 2026"})

# ---------------- SERVICEFIRST ----------------
S=[(U,"File is a campaign plan; no sales history")]*7+[(U,"No price or guarantee in md; \"pilot ends about 3 Dec\""),(U,"Not in md"),(X,"Not in md"),(U,"Not in md; a \"pilot\" exists")]
S+=[(D,"[research doc] \"Client Hub ServiceFirst tenant\""),(U,"Not in md"),(U,"Not in md"),(D,"Fireflies client calls 27 Aug to 23 Oct; SERVICEFIRST_CONTEXT_DO_NOT_DELETE.md"),
(D,"SmartLead, CloudTalk, White Whale, Client Hub in use"),(U,"Not in md"),(U,"Mailbox domains exist; order date not in md"),(U,"Not in md"),(D,"Client calls 27 Aug, 10 Sep, 1 Oct, 16 Oct, 23 Oct"),
(D,"White Whale signals audited 23 Oct (most were noise)")]
S+=[(D,"\"campaign plan, diagnosis and overhaul PDFs\"; context file"),(D,"B1 to B7 lists"),(D,"Blitz/Pronto/LeadsForge data"),(U,"B2 \"Open signals\"; White Whale"),
(N,"\"22 of the 40 non-OOO replies say the person left\"; only B7 validated"),(D,"Copy \"rewritten three times\""),(N,"B6/B7 break house rules; B6 step 3 blank subject"),
(U,"Not in md"),(D,"B1 to B7 built"),(U,"Not in md")]
S+=[(D,"B1 to B7 live"),(U,"Not in md"),(D,"1,396 call activities"),(U,"\"None has a note or disposition logged\""),(U,"Not in md")]
S+=[(N,"SmartLead \"interested\" flag stale"),(D,"\"one meeting ever\" (General Assembly, not qualified)"),(N,"Reputation 41 to 63% late Sept, \"one Gmail domain was blacklisted\""),
(D,"Client calls every 2 to 3 weeks"),(D,"Three new concepts proposed"),(D,"\"B3 ABM (archived)\""),(U,"Not in md")]
S+=[(U,"Not in md"),(U,"1 meeting in 2 months; promise not in md"),(U,"Concept 1 tied to renewal (question)"),(U,"Not in md"),(N,"\"The pilot ends about 3 Dec and ServiceFirst raised an early-ending concern\"")]
S+=[(X,"Active client")]*5
SC=[(D,"ServiceFirst tenant referenced"),(U,"Not in md"),(U,"Not in md"),(U,"Not in md"),(U,"Not in md"),
(U,"Only \"named for suppression only: Reprise Financial and SHEIN\" and \"existing list\" of disqualifiers; blacklist load not in md"),(U,"Not in md"),
(U,"Not in md"),(U,"Not in md"),(D,"Client calls recorded from 27 Aug"),(D,"SERVICEFIRST_CONTEXT_DO_NOT_DELETE.md (Helper not mentioned)"),
(U,"Not in md"),(U,"Domains exist; DNS/warm-up not in md"),(U,"Not in md"),(D,"Campaigns B1 to B7 in SmartLead (tagging not in md)"),
(U,"Senders Marvielyn and Charrisse proposed; live status not in md"),(U,"Not in md"),(N,"CloudTalk used; \"None has a note or disposition logged\""),(U,"Not in md"),(U,"Not in md"),
(D,"White Whale signals audited; plan says turn most off"),(U,"Not in md"),(D,"Regular client calls"),(D,"Plan PDFs and context file"),(U,"Not in md"),(U,"Copy rewritten 3 times; approvals not in md"),
(U,"Not in md"),(D,"BDRs calling (\"BDRs say the competitor list is the best to call\")"),(D,"B1 to B7 live"),(U,"Start date not in md")]
mk("servicefirst",S,SC,{"name":"ServiceFirst","tenant":"not given in md","state":"active pilot, ends about 3 Dec 2026","raw_date":"prepared 3 Nov 2026","note":"Source file is a next-campaign research plan, not a full client history, so most onboarding items are unclear."})
