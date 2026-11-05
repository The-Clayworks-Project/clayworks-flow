# Variolytics: complete client history (signing to 4 Nov 2026)

Compiled 4 Nov 2026 for Joy. Sources:
- Drive (the Variolytics folder and Joy's folders) and local files in `Clayworks/Variolytics/`
- Slack, Fireflies and Calendar
- Client Hub (CSM, ops board, meetings, metrics, blacklist)
- The SmartLead API (all 16 Variolytics campaigns)
- Joy's own Claude working sessions from 6 Oct to 4 Nov

This was a read-only sweep; nothing was changed anywhere. Tags: **[confirmed]** in a primary system, **[inferred]** my reading, **[conflict]** sources disagree.

> **Status in one line:** the client is still active and not closing. Outbound is on a long-term contract that renews 31 Dec 2026. The Paid Ads pilot renews or ends 30 Nov 2026. Account health is **43, red, "At Risk" since 27 Oct**. The client is happy with meeting quality, but needs about 2x the volume (30+ meetings a month against an average of about 13).

---

## 1. The client in brief

| | |
|---|---|
| Company | Variolytics, a German clean-tech company |
| Product | **EmiCo Lite**, a tank-mounted off-gas sensor. It measures N2O, CH4, CO2 and O2 above the aeration tank of a wastewater plant. N2O only forms during nitrification/denitrification (BNR), so **no BNR means no fit**. |
| Two value stories | **Municipal plants:** real N2O measurement versus estimates, ahead of the recast EU UWWTD reporting rules. **Commercial/industrial plants:** aeration energy (blowers are about half of a plant's power bill), with 10-20% over-aeration savings. |
| Client deal size | About EUR 40k ACV, close rate about 0.4 (Hub, for ROI maths) |
| Client sales capacity | About 60 of 100 units sold for the year (9 Sep). They budget about 100 meetings a month across all sources; their own BDRs book about 10 a month. |
| Client situation | Q3 missed target, investor pressure, "considering a small funding bridge" (13 Oct). Most closes start as trials. |

### People

**Client side**
- **Nicolaj (Hagemann) Snabe ("Nic/Nick")**, Head of BD. He takes most meetings, is the sender persona on all 18 mailboxes, and signs off on any reference use. Very busy and slow on email. He moved to Denmark in Oct.
- **Johan Barlach.** Takes the Dutch and ads meetings and is a LinkedIn sender. One Hub comment calls him "client CEO" **[conflict: CEO or not unconfirmed]**. He refused to share CRM data.
- **Judith Serafin**, Head of Marketing. Owns the ads contract and was "hardball" at the last meeting (28 Oct).
- **David Hoffmann**, sales engineer. Takes German meetings and had his LinkedIn onboarded on 1 Oct.
- **Mattias** is a LinkedIn sender. **Yann** is the client's CRM manager.

**Clayworks side**
- **Callum** and **Theo** are the primary owners on the Hub. Callum was the BDR from Mar to May and runs the client check-ins.
- **Agnes Sacher** is the Clayworks BDR who books Variolytics meetings by phone from June onward. **Note: Agnes is ours, not the client's.**
- **Joy** owns campaign builds from the week of 26 Oct (handover started 6 Oct; knowledge test passed 22 Oct). The target is full ownership by day 90.
- **"Jack Page"** (jack@clayworks.io) speaks on every client call. The Slack account with that email is named "Theo", so it is most likely Theo's client-facing name **[inferred: confirm]**.

---

## 2. Commercial terms

| Item | What we know | Source |
|---|---|---|
| Outbound contract start | **25 Feb 2026** | Hub CSM **[confirmed]** |
| Outbound renewal | **31 Dec 2026** | Hub CSM |
| Outbound guarantee | **15 meetings a month**, monthly cycles with a catch-up every 14 days. **Now in cycle 9** (10 days left on 4 Nov). | Hub CSM, 4 Nov stand-up |
| Contracting entity | The Clayworks Project LLC, under Wyoming law | Theo to Judith, 15 Jul |
| Fee | Only one data point: the March P&L shows "Clayworks Complete" income of **£4,500**, with £220 of pass-through costs. It is unclear whether this is monthly. | Tracker sheet **[inferred]** |
| Invoicing | Moved to a 14-day, two-week cycle (22 Sep / 13 Oct) | Fireflies check-ins |
| **Paid Ads pilot** (second deal) | Pitched 25 Jun. Judith redlined it and Theo replied on 15 Jul: **fixed 3-month pilot, no auto-renewal**, formal end-of-pilot review, KPIs directional not guaranteed. Kickoff 1 Sep, live 11 Sep. Hub: guarantee 10 meetings a month, **renews 30 Nov 2026**. Prime Marketing (Papillon) delivers it as a subcontractor and invoices Clayworks. | #prime-marketing, Fireflies, Hub CSM |
| Missing | The signed contract itself (price, term, notice period), the 14-page "Account Handover Handbook", and the sales call recording (Fireflies starts 25 Jun). **Ask Theo/Callum.** | |

---

## 3. Onboarding (Mar 2026)

- **Infrastructure, set up 1 Mar:**
  - 9 sending domains: variolyticsai, variolyticswater, variowaste, variomonitor, varioinsight, variolyticsdata, variolyticsiq, variowastetech and variowater (.com), on Cloudflare, forwarding to variolytics.com.
  - **18 mailboxes** (8 Microsoft, 10 Google, from InboxKit), all sending as "Nicolaj Snabe".
  - 2 Prosp LinkedIn licences and 2 CloudTalk numbers.
  - Capacity is about 18 x 25 a day, or about 9,900 emails a month.
- **Hub tenant** created 11 Mar. Drive folder created 6 Mar.
- **Onboarding doc ("Plan of Action"):**
  - Start with **Nordic municipal WWTPs** (Sweden, Norway, Finland).
  - Personas: Plant/Operations Manager, Environmental Compliance, Sustainability/ESG.
  - Qualify at **>10,000 PE plus BNR present**.
  - Success means pilot proposals or booked site visits in the first 90 days.
  - The client said **no to name-dropping**.
  - Meetings book through the client's **Pipedrive scheduler** on MS Teams.
- **Blacklist** at onboarding: 132 entries uploaded. It now has **167**: 123 existing customers, 24 do-not-contact, 20 opt-outs.
- **Never contact:** Severn Trent (cite only), Waternet, Waterschap Limburg and Veolia. Hafren Dyfrdwy only with Nic's OK. Also exclude competitors (Xylem, E+H, Hach, Innovyze, Purecontrol, Unisense, Horiba, Binder, Upwater) and existing customers (e.g. BASF, LyondellBasell).
- **References:** Severn Trent UK (19 units, cite but never email), VA SYD (Sweden/Denmark only, Nic signs off), Aquafin BE and Aarhus DK. **Nothing is cleared for Germany.**
- **Security flag:** the tracker sheet's "Domains & Mailboxes" tab holds **plaintext passwords and app passwords for all 18 mailboxes** on a shared drive. These should be moved and rotated.

---

## 4. Campaign history, phase by phase

### Phase 1, Mar to Jul 2026: municipal WWTPs (N2O and compliance angle)
6-step sequences on SmartLead plus matching Prosp LinkedIn campaigns. Callum booked from March to May and Agnes from June.

| SL id | Campaign | Start | Leads | Sent | Replies | Bounce | Positive |
|---|---|---|---|---|---|---|---|
| 3039770 | Sweden B1, WWTP, all except ops | 15 Mar | 500 | 2,570 | 33 (6.6%) | 8.4% | 11 |
| 3048048 | Sweden B2, ops only ("wrong person?") | 17 Mar | 101 | 479 | 4 | 9.1% | 2 |
| 3120037 | Norway, high-intent signals (per-lead copy) | 2 Apr | 42 | 188 | 6 (14%) | 21% | 2 |
| 3204154 | Norway B1 (reused Sweden copy) | 20 Apr | 147 | 834 | **0** | 6.8% | 0 |
| 3242088 | Poland B1 (UWWTD compliance) | 27 Apr | 205 | 1,172 | 3 | 7.8% | 2 |
| 3242075 | Poland B2, ops only | 27 Apr | 59 | 286 | 3 | **49%** | 1 |
| 3406075/77 | Finland B1 / B2 | 27 May | 97 | 526 | 0 | ~10% | 0 |
| 3598660 | UK B1 (per-lead copy) | 6 Jul | 60 | 325 | 2 | 3.3% | 1 |
| 3599210 | Netherlands B1 | 6 Jul | 50 | 256 | 4 | 3.7% | 1 |

- **The original offer stack** (Sweden v8, March) escalated over 6 emails: a free N2O audit, then a free aeration report, a free 8-week baseline and a free UWWTD readiness check, ending with "Year 1 hardware free, software fee only".
- **Lessons:**
  - List quality matters more than copy. Norway B1 reused the Sweden copy and got 0 replies.
  - The best step-1 subject was "N2O peaks at {co}?".
  - The "Closing the file on {co}" A/B/C close works.
  - English works everywhere except Poland.
  - **Most meetings came from calls, not email**: 27 of the tagged meetings are from calls, 8 from email.

### Phase 2, Jul to Sep 2026: shift to commercial/industrial plants (aeration energy angle)
- **The pivot (Weeks 18 to 20 check-ins):**
  - Industrial lists of chemicals, dairy, pulp and paper, and refineries.
  - The client built an energy-savings estimator and ROI calculator (live 7 Aug).
  - The German industrial offer was a free test with purchase tied to proven savings.

| SL id | Campaign | Start | Leads | Sent | Replies | Bounce | Positive |
|---|---|---|---|---|---|---|---|
| 3742650 | Commercial Plants Germany Aug (**German language**, 18 mailboxes) | 30 Jul | 279 | 1,125 | 7 | **21.5%** | 1 (Andechser) |
| 3953029 | Commercial Plants Sweden Sep | 14 Sep | 1,032 | 3,845 | 63 (6.1%) | **15.1%** | 4 |
| 3953030 | Commercial Plants Denmark Sep (finished 26 Oct) | 14 Sep | 511 | 2,150 | 39 (7.6%) | **17.2%** | 3 |

- Results:
  - The DK/SE commercial campaigns produced about 7 meetings by 22 Sep and finished at a 6-8% reply rate.
  - **German recipients complained** (9 Sep). It was handled by blacklisting their domains.
  - Callum, 16 Oct: the commercial LinkedIn campaign had "a lot of not fits", meaning no own wastewater treatment.
  - That is what led to the BNR filter.

### Phase 3, Oct to Nov 2026: Joy's rebuild and the "pump the numbers" push
**Timeline**
- **6 Oct:** handover from Theo to Joy. The Prosp LinkedIn lists for Sweden and Denmark were rebuilt (1,423 contacts) for Johan and Mattias.
- **15 Oct:** Joy + Jack sync. The offer was confused (commercial and municipal swapped).
- **22 Oct:** Theo's direction:
  - Split Germany into two campaigns, commercial and municipal.
  - Make the BNR filter repeatable.
  - Aim for 1,000+ companies.
- **23 Oct, offer confirmed:**
  - **Municipal:** 12 months free (software or hardware, still ambiguous).
  - **Commercial:** 3 months with everything free.
- **27 to 28 Oct:**
  - Germany drafts built.
  - Theo's copy review asked for a formal tone, the full-name signature "Nicolaj Hagemann Snabe, Head of Business Development", energy-only for commercial, no company name in subjects, and a kWh ask that leads into the ROI calculator.
  - Lists were grown with Blitz, Pronto, website scrapes and email patterns.
  - The Germany commercial touch 1 hook went to sector lines ("Dairies that clean their own wastewater spend more on aeration than on anything else in that plant").
- **28 Oct, client check-in (Week 32):**
  - Nicolaj needs **30+ meetings a month**.
  - A Danish cold-calling agency books them **about 50 a month** and may get commercial too.
  - Nicolaj had not seen the ads.
  - The rescheduled pipeline was cut from about 700k to about 350k.
- **29 Oct:** Theo: "pump the numbers". The Europe-wide commercial campaign was created.
- **30 Oct, BNR filter v0.1 to v0.5.1** (skill + process page + runbook):
  - Plants are scored from the EU E-PRTR/IED register: A = direct discharge plus nitrogen, B = direct discharge, C = off-site transfers only.
  - A website scan finds phones and BNR evidence.
  - Results on the live Germany commercial list: A 45, B 152, C 613, D 21, not in register 1,030.
- **30 Oct to 2 Nov:** Europe built to 3,772 leads.
  - Copy cleaned: no "Most..." lines, new step-5 close. The Germany copy was left unchanged, per Joy.
  - 4 vendors removed.
  - Two Pronto/Pipecorn rounds added 1,251 + 212 leads (Deliverable + Catch-All kept).
- **2 to 3 Nov, mailboxes RED:**
  - 6.0% bounce, 3.62% reply, 0 spares.
  - 3 mailboxes rested at 16-25% bounce (nicolajsnabe@variolyticsiq.com at 24.6%).
  - 2 spare Nicolaj mailboxes added to Municipal.
  - Joy & Theo: no extra mailboxes to be bought.
- **4 Nov:**
  - Hub plans set live.
  - Nick swapped for David on the Germany commercial LinkedIn campaign.
  - Denmark closed out.
  - Blacklist check of all live SmartLead campaigns: clean, apart from one InfraServ Höchst lead flagged as a likely customer operator.
  - Variolytics is the **top delivery priority**: cycle 9, minimum 15, Agnes aiming for 17.

**Live campaigns (4 Nov)**

| SL id | Campaign | Target and build | Leads | Sent so far | Replies | Bounce | Mailboxes |
|---|---|---|---|---|---|---|---|
| 3953029 | Commercial Plants **Sweden** (Sep) | Theo's build, follow-ups only. Finishes about 20 Nov, then its 2 mailboxes move to Europe. | 1,032 | 3,845 | 63 | 15.1% (lifetime) | 2 |
| 4249417 | Commercial Plants **Germany** (Nov) | Register-led accounts (thru.de + state lists), then people (Blitz/Pronto/web). Energy-only, 5 steps. | 1,861 | 714 | 19 | 7.5% | 5 (1 rested) |
| 4249556 | **Municipalities** Germany (Nov) | Operators of plants >10k PE, website-sourced (staff not on LinkedIn). N2O angle, 12 months free. | 1,002 | 230 | 10 | **11%** | 3 (2 rested, 2 spares added) |
| 4266958 | Commercial Plants **Europe** (Nov), 13 countries | Blitz per country plus the BNR filter. FR 653, IT 451, GB 397, ES 377, SE 289, BE 285, NL 273, AT 259, FI 228, IE 160, CH 143, NO 129, DK 128. About 1,850 companies; BNR tier A 152, B 315. | 3,772 | 519 | 13 | 5.8% | 7 |

- **Where the bounces come from:**
  - Municipal: website-scraped emails (9 of 17) and untagged emails (8 of 17).
  - Germany commercial: untagged emails (23 of 28).
  - Pronto and Blitz emails rarely bounce.
- **LinkedIn (Prosp), as synced in the Hub:**

| Campaign | Status | Leads |
|---|---|---|
| Sweden & Denmark Commercial | active | 1,423 |
| Germany Municipalities | active | 384 |
| Germany Commercial | stopped (Nick's LinkedIn disconnected; David swapped in 4 Nov) | 1,691 |
| Referral Workflow | active | |

Older LinkedIn campaigns are stopped.

### All-time SmartLead totals (16 campaigns)
- **Volume:** 9,718 leads and 15,219 emails sent.
- **Replies:** 206 (4.9% of people contacted).
- **Bounces:** 517 (12.3%).
- **Positive:** 9 Interested, 1 Meeting Request and 18 Information Requests.
- **Other categories:** 314 sender bounces, 174 out-of-office, 50 wrong person, 25 not interested and 10 do-not-contact.
- In the Hub, email positive replies fell to about 1 a month in Oct and Nov, at the highest volume yet.

---

## 5. Paid Ads (Prime Marketing as subcontractor)
- **Channels:** Google Search, LinkedIn ABM and Meta retargeting. The ads use the energy-optimisation angle.
- **First 3 weeks (29 Sep):**
  - 5,000 ICP accounts reached, 600 site visitors.
  - 79% of high engagement came from NL.
  - Google: €1k for 370 visits.
  - Dutch ads started in early Oct.
- **By 28 Oct:** 13-14 leads and 2 meetings, with only about €2k of a **€10k/month** budget spent. The client "now spends more than double on ads".
- **Recent ads leads and meetings:** EMECO (ES), TEW Servicegesellschaft, TYPSA Murcia and Cetaqua.
- **Risk:** Prime Marketing has churned as a Clayworks client (offboarding 13 Oct) but still runs the Variolytics ads. A VAT issue on Prime's invoice was fixed on 15 Oct by using Clayworks' US address.

---

## 6. Results

| Metric | Value | Source |
|---|---|---|
| Meetings, 25 Feb to 4 Nov | **77 records**: 34 held, 32 qualified, 3 not qualified, 8 cancelled, 1 no-show, 16 rescheduled, 18 scheduled | Hub meetings |
| Pipeline | **EUR 2.63M** (Hub snapshot); €2.6M with 68 booked / 31 qualified (3 Nov call script) | Hub, call script |
| Closed won | **2**: Nedre Romerike Vann (NO, Apr) and Turun seudun puhdistamo (FI, Jul). On 24 Aug, 2 were closed and 1 was cancelled. | Hub, Week 23 call |
| Average | About 12-13 meetings a month (Theo/Jack); guarantee is 15 | Fireflies |
| Bookings per month (Hub) | Mar 3, Apr 11, May 8, Jun 12, Jul 9, Aug 7, Sep 13, Oct 11, Nov 1-4: 3 | Hub |
| Sales case study used by Callum | "€2.4M pipeline in 5 months from 56 meetings, 86% qualified" | 28 Sep pitch **[conflict: 56 / 68 / 69 / 77 counts across sources]** |
| Upcoming meetings | Jacobs (3 Nov); WiK Krzeszowice and Eliquo Hydrok (9 Nov); Rose Poultry (16 Nov); TEW (19 Nov); ZWiK Września (23 Nov); TYPSA and Erftverband (24 Nov); Waterschap Limburg (25 Nov) | Hub |

**Waterschap Limburg is on the client's never-contact list** but has a meeting booked on 25 Nov from email. Check this.

**Held meetings by phase:**
- Mar to May, Nordic municipal: Trollhättan, Gryaab, Falköping, Nedre Romerike (won), Håbo, Ängelholm, Uppsala, Nyköping, Kalmar, Borås (offer sent), Arboga, Oskarshamn.
- Jun to Aug, Poland/Finland/Sweden: Węgrów, Kuopio, Jaworzno and PEWIK Gdynia (quotes requested), RCGW, EKO-Raszyn, Vihti, BWiK, Vivab (may close), Mott MacDonald Bentley, Turku (won), Joensuu, Vimmerby, Stockholm Vatten, EasyMining.
- Sep to Oct, commercial: MEGGLE, MWiK Bydgoszcz, Südzucker, Bioceval and Skånemejerier qualified; Nouryon not qualified.

---

## 7. Recurring problems and lessons
1. **Bounces are the main email problem:**
   - Poland B2 49%, Germany Aug 21.5%, DK/SE commercial 15-17%, Municipal Nov 11%.
   - The cause is unverified, scraped or pattern-built emails, not the copy.
   - Fix: verify before sending, keep Pronto/Blitz-verified emails, and keep Catch-All emails (Joy's rule).
2. **Fit:** many commercial sites don't run BNR. The BNR filter (register first, then website and people signals) is now the standard. Build **accounts first, then people**.
3. **Calls beat email** for booking. Phones from websites go on Client Hub contact cards.
4. **No-shows and reschedules**, especially in Poland. The rule is to cancel after 2-3 failed reschedules within a two-week window.
5. **LinkedIn accounts keep disconnecting** (Nick on 28 and 30 Oct) and booking pages keep breaking (David's page on 6 Oct, a calendar alert on 30 Oct).
6. **Germany legality:**
   - UWG §7 suggests German B2B cold email needs prior consent. Theo raised it on 27 Oct.
   - On 3 Nov, Clayworks excluded Germany from its own Project Mayhem push "because of legal risk".
   - Meanwhile the Variolytics German email campaigns are live. **This is unresolved.**
7. **Data hygiene:**
   - Hub meeting counts don't match reality (Agnes's bug card).
   - 16 "rescheduled" records have no outcome.
   - No call metrics are logged.
8. **Copy rules** (Joy/Theo): no em dashes, ninth-grade language, every touch a new thread with an internal-style subject, no "Most..." lines, no "last email", and no product terms in subjects. Germany copy is formal with the full-name signature.

---

## 8. Risks and churn signals
| Risk | Detail |
|---|---|
| Volume gap | Need 30+ a month; delivering about 13. Investor pressure. Nicolaj asked for a "step change". |
| Competitor | A Danish multilingual calling agency books about 50 a month for them (mostly municipal) and may get commercial too. |
| Ads renewal 30 Nov | Fixed pilot, no auto-renewal, formal review. Ads health is red (43). Judith is a tough negotiator, and the delivery partner (Prime) has churned from Clayworks. |
| Client finances | Considering a funding bridge. Prospects are pushing purchases into 2027. |
| Deliverability | Mailboxes RED, 3 rested, no spare budget for new mailboxes. |
| Legal | German cold email under UWG. |
| Clayworks capacity | Clayworks revenue fell from about $48k to $18k (3 Nov) and the team is stretched. Variolytics is now the top-priority account. Losing it would hurt. |

No cancellation or notice from Variolytics was found anywhere.

---

## 9. Open items (4 Nov)
**Ops / CSM tasks**
- Reschedule or cancel stale meetings and update the pipeline (Callum, 6 Nov).
- Send Nic examples of the LinkedIn ads (Callum, 6 Nov).
- **Client:** reconnect Nick's LinkedIn (6 Nov).
- Pipedrive integration setup call with the client's CRM manager (Theo, in progress, due 6 Nov; overdue since 19 Oct).
- Add an "on trial" pipeline stage, a CRM scoping call with Nic + Johan, and the Germany email + LinkedIn launch (Callum, 12 Nov).
- **Client:** send updated plant lists for NL, UK and DE, and name a CRM contact (12 Nov).
- Next client check-in: **12 Nov (Week 34)**.

**Joy's queue**
- Mailboxes: plan approved by nobody yet ("hold off", 3 Nov). Options:
  - Pause and verify the risky not-started leads in Municipal and Germany commercial.
  - Point Sweden's 2 mailboxes at Municipal instead of Europe on 20 Nov.
  - Bring the 3 rested mailboxes back at 10 a day.
- InfraServ Höchst lead (Germany commercial): likely an existing-customer operator. Remove? Waiting on Joy.
- Prosp: check whether the Sweden/Denmark LinkedIn campaigns still contain 4 blacklisted people (Palsgaard, Daniatech, Campus by Nordrest x2).
- Agnes's feedback on the Europe BNR leads, then iterate the filter and decide on a country top-up (PL, PT, HU, RO, Baltics) or going deeper.
- Name extraction from 1,162 website "people" snippets. Put phones on Hub contact cards.
- Theo reviews the BNR dataset before anything new goes live.
- Rotate the SmartLead and Prospeo keys. Remove the plaintext mailbox passwords from the tracker sheet.

**Unknowns to chase**
- The signed outbound contract (price, term, notice).
- The exact ads review date.
- Whether "Jack Page" is Theo.
- The municipal offer wording ("software or hardware").
- The qualified-meeting definition.
- The outcome of Vivab and the 28 Oct "may close this week" deal.
- Waterschap Limburg (never-contact list) booked for 25 Nov.

---

## 10. Where things live
- **Drive folder:** https://drive.google.com/drive/folders/1Jl9H6oZJ9MbYgeu1RbeNePWueZG46fKq
  - Onboarding doc: https://docs.google.com/document/d/1CQLJxJBkKQqIBnasRm-BUeniHXrEJcR-yII7EqxUk68
  - Tracker (P&L, campaigns, mailboxes; contains credentials): https://docs.google.com/spreadsheets/d/14Qr974HcjLtEDn0p_wOaptylXLkgcbWFw_f1J8Z6Snw
  - Collateral: cheat sheet, top references, glossary, cold call scripts (incl. the German Leitfaden), the EmiCo Lite PDFs (incl. Polish) and the client reference list (6 Feb 2026).
  - Five shortcuts in the folder can't be opened from Joy's account: breakdown, buying signals, Data Bases, Compliance, Script.
- **Joy's handoff docs:**
  - Campaign Handoff 27 Oct: https://drive.google.com/file/d/1f6iF8MIF8PeEGt_rF3mMoav0bS5wZUvS
  - Sourcing Brief 27 Oct: https://drive.google.com/file/d/1MyB3zAHKpRxnpBQ91ngP-IP9WZTYx_t-
- **Local, `Clayworks/Variolytics/`:**
  - Copy and briefs (Germany commercial v2 / v4, municipal v1 + messaging brief, side-by-side).
  - Every upload batch CSV (DE commercial batches 2 to 6, DE municipal batches 1 to 9, Europe rounds).
  - Pronto find-email files and the Prosp LinkedIn files.
  - The knowledge-test study sheet and quiz.
- **BNR filter:**
  - `Variolytics/BNR_filter/` (process page v0.5.1, README, Germany sites, website scan).
  - The skill: `~/.claude/skills/variolytics-bnr-filter`.
  - The runbook: `runbooks/02_variolytics_bnr_filter.md`.
- **Systems:**
  - Client Hub tenant `009782d9-ce56-40ed-bd66-b7035ced02f7`.
  - SmartLead campaigns listed above.
  - Prosp for LinkedIn.
  - Slack: no client channel. Ads talk is in #prime-marketing. Delivery talk is in #csm, #operations and DMs; bookings go to #all-clayworks.
