# ASF Nonprofit Brand and Editorial Audit

**Document ID:** ASF-OPS-AUDIT-001  
**Version:** 0.1  
**Public-source review date:** 15 November 2026  
**Status:** Advisory assessment for leadership and volunteer coordinators; recommendations are not adopted policy.  
**Scope:** Nonprofit communications, editorial governance, public trust, safeguarding, and member experience. No application changes are authorized by this document.

## Executive summary

ASF has an authentic and welcoming community proposition: women connecting through surfing, learning, mutual support, and social action. The founder story, references to past community activities, free learning guides, and several carefully qualified partner offers provide useful foundations.

The principal weakness is not a shortage of content. It is that visitors can receive incompatible explanations of how ASF works. The published funding model promises no advertising, subscriptions, premium plans, or paywalls. Public Terms, Cookie Policy, and Privacy Policy still describe advertising or AdSense. Sponsorship copy offers commercial-style visibility, while the homepage presents a more restrained, benefit-led partnership model. Membership privacy explanations also describe different registration arrangements.

**Leadership priority:** settle the governing position, confirm actual practices, and then align the public explanations. Merely removing uncomfortable wording would not resolve a mismatch between a promise and practice.

This review does **not** establish that advertising is currently served, that personal data has been exposed, that membership verification fails, or that nonprofit governance is absent. Those questions require different evidence. It identifies published contradictions and missing explanations that leadership can address through a controlled, documentation-led process.

### Five decisions to make first

1. What does ASF mean by zero advertising, and what limited, neutral supporter acknowledgment is compatible with that promise?
2. Which registration process is current, and what does a Carteirinha confer beyond participation in the community?
3. Who can approve organizational claims, partnerships, safety-sensitive material, and corrections?
4. Which community visibility, image-consent, moderation, and safeguarding rules apply before someone publishes or joins an activity?
5. Which document is authoritative when public policies, partner materials, and historical planning notes disagree?

### Companion documents

- [Proposed Zero-Ad Governance and Partnership Charter](ZERO_AD_GOVERNANCE_AND_PARTNERSHIP_CHARTER.md): approval-ready policy, not a claim of existing ratification.
- [Bilingual Content and Localization Style Guide](CONTENT_AND_LOCALIZATION_STYLE_GUIDE.md): practical writing, review, terminology, and metadata standards.

## 1. Method, evidence, and limitations

### 1.1 What was reviewed

The assessment used Exa to retrieve readable text from 22 public URLs, including both homepage addresses, About, partnerships, sponsorship, benefits, member entry points, public policies, all five core learning articles under Aprender, and one mental-health article. Selected public repository documentation and page copy were also reviewed through read-only GitHub access.

The review did not submit forms, create memberships, upload images, send confirmation emails, access private member records, or test financial transactions. Firecrawl was not used. This is not a legal opinion, clinical review, security assessment, advertising-network inspection, or accessibility certification.

Two alias URLs, `/carteirinha/` and `/patrocinio/`, returned empty content to the crawler. Public repository copy identified their intended destinations, which were read separately. An empty extraction is not proof of a broken visitor journey.

Some homepage text belongs to hidden or dynamic sections. Findings about that text are a copy-inventory warning, not proof that all visitors see every passage. The Mural extraction was particularly sparse; its public repository form copy was examined as a supplement. No conclusion about server-side moderation follows from that form review.

### 1.2 Evidence labels

- **Observed:** a statement or omission in the reviewed public material.
- **Interpretation:** a plausible consequence for understanding or trust, not a measured user outcome.
- **Verify:** a question requiring leadership, operational, legal, or specialist confirmation.
- **Recommended:** a proposed change or control; not a description of an existing ASF practice.

Numbers, superlatives, and health claims are described as unsubstantiated in the reviewed material when supporting evidence was not visible. That is not an allegation that they are fabricated.

### 1.3 Publication provenance

These documents are published only in the account holder's fork. The publication baseline is fork `main` at `dd22ce1cbba4bfd02f09a37a3730d39220aa2131`. The upstream reference checked for context was `0373c4cb339a4d1833c83e8768bddc4e2a74eeef`. The fork was intentionally not synchronized with upstream application changes. Findings concern the public sources reviewed, not an assertion that every file in the older fork matches the live website.

## 2. Strengths worth preserving

| Strength | Why it matters | Evidence |
|---|---|---|
| Welcoming community voice | The message centers belonging rather than competition or purchasing. | [Homepage](https://asf.surf/) |
| A specific origin story | Named founders, a chronology, and linked records make the community more tangible. | [About ASF](https://asf.surf/sobre.html) |
| Direct-payment boundaries | The homepage says ASF does not sell products, charge monthly fees, or intermediate partner payments. | [Homepage partnership sections](https://asf.surf/) |
| Written partnership approval and qualified benefits | The homepage avoids guaranteed reach; the benefits page separates confirmed conditions from negotiations. | [Homepage](https://asf.surf/) and [Benefits](https://asf.surf/beneficios/) |
| Improved learning-article framing | Core guides include intended audience, an objective, reading estimate, revision date, and limitations. | [Beginner guide](https://asf.surf/aprender/como-comecar-a-surfar-mulheres.html) |
| An understandable local-storage explanation | The Diário FAQ tells readers where entries are said to remain and mentions backup and restoration. | [Diário](https://acarolmourad-commits.github.io/asf-diario/) |
| Existing editorial discipline | Repository rules already call for checking duplicates, identifying authoritative sources, and correcting conflicts. | [Editorial rules](https://github.com/acarolmourad-commits/asf-app/blob/0373c4cb339a4d1833c83e8768bddc4e2a74eeef/docs/EDITORIAL-RULES.md) |

## 3. Finding F01: the zero-ad mission and public policies conflict

**Priority: P0 — resolve before repeating an unqualified zero-ad promise.**

The [funding model](https://github.com/acarolmourad-commits/asf-app/blob/0373c4cb339a4d1833c83e8768bddc4e2a74eeef/docs/MODELO-SUSTENTACAO.md), effective according to its own text from 24 September 2026, states that content is free, without subscription, paywall, premium plan, or ads. It identifies business support, partner donations, and confirmed member benefits as support mechanisms.

| Public source | Observed wording or position | Why leadership must reconcile it |
|---|---|---|
| [Terms, section 5](https://asf.surf/termos-de-uso.html) | Says the app displays partner links and third-party advertising, including Google AdSense. | Reads as an affirmative description of advertising, not a zero-ad commitment. |
| [Cookie Policy](https://asf.surf/cookies.html) | Describes optional advertising and loading AdSense after an explicit optional-cookie choice. | Consent to optional processing does not itself resolve the mission question. |
| [Privacy Policy, sections 4–5](https://asf.surf/privacidade.html) | Describes advertising services, including AdSense, and technologies for metrics or advertising. | Allows a broader practice than the funding promise suggests. |
| [Content plan](https://github.com/acarolmourad-commits/asf-app/blob/0373c4cb339a4d1833c83e8768bddc4e2a74eeef/docs/PLANO-CONTEUDO.md) | A plan dated 2 October 2026 explicitly links content growth to AdSense monetization. | A current-looking operational objective conflicts with the earlier no-ad position. |
| [AdSense preparation note](https://github.com/acarolmourad-commits/asf-app/blob/0373c4cb339a4d1833c83e8768bddc4e2a74eeef/docs/ADSENSE-READY.md) | Presents an advertising-readiness path. | Volunteers can mistake it for an approved direction unless its status is made clear. |

**Recommended control:** leadership should record the approved model and commission a separately scoped check of actual practice. Public explanations must then describe the verified practice. Historical documents should be clearly labeled as historical or superseded rather than silently treated as current instructions.

**Acceptance test:** a newcomer and a volunteer can independently explain what is free, whether ASF carries ads, how ASF receives support, and why optional partner purchases are different from ASF access.

## 4. Finding F02: nonprofit purpose is uneven across entry points

**Priority: P1 — make purpose understandable before asking for participation or brand support.**

The [homepage](https://asf.surf/) contains strong nonprofit and no-monthly-fee language, but much of it is inside partnership-oriented content. Its opening emphasizes community and surfing. The [About page](https://asf.surf/sobre.html) is rich in history but does not provide a similarly concise present-day explanation of free access, funding, current accountability, or membership rights.

**Interpretation:** a visitor may understand that ASF is welcoming without understanding its nonprofit operating model. A brand may find a clearer explanation of the organization than a prospective member does.

**Recommended hierarchy:** purpose and audience; what is free; four member actions; community and social impact; partners and funding; governance, privacy, and help. A short, consistent mission line is preferable to repeating a long institutional statement on every page.

**Verify before drafting:** the official organizational name, legal status and registration if applicable, current responsible roles, geographical scope, and the difference between historical activities and programs currently offered. Do not imply a formal registration, a board composition, or active services that have not been confirmed.

## 5. Finding F03: partnership benefits, donor recognition, and advertising blur together

**Priority: P0 for policy boundaries; P1 for individual listings.**

The homepage describes voluntary member benefits, direct partner purchases, written approval, no sharing of the member database, and no guaranteed reach. Those are good safeguards. The separate [sponsorship page](https://patrocinio.asf.surf/) offers fixed logos across apps, continuous visibility, exclusivity, and activation commitments. It also shows percentage, audience-engagement, and popularity claims without visible substantiation.

Sponsorship can support a nonprofit, but calling a placement support does not automatically make it non-advertising. Leadership needs a substantive test: is this a neutral acknowledgment of support, or is ASF selling promotional access to its audience?

### Required distinctions

1. **Supporter acknowledgment:** factual identification of support in a bounded credits area; no product persuasion or promised exposure.
2. **Member benefit:** a practical, optional offer with confirmed eligibility, dates, costs, and conditions; no sales commission or paid ranking under the proposed charter.
3. **Editorial reference:** a source or example chosen for educational value, independently of funding.
4. **Commercial promotion:** purchased visibility, sponsored recommendations, acquisition promises, paid priority, or audience targeting; incompatible with the proposed zero-ad standard.

The [Surfmappers page](https://asf.surf/parcerias/surfmappers/) describes an annual-plan discount for partner businesses entering Surfmappers Experience. It should not be presented as a universal member discount or as an ASF subscription. The [benefits page](https://asf.surf/beneficios/) provides a stronger pattern by qualifying confirmed offers and noting that conditions must be checked directly.

**Verify:** approval records, public permission for coupon publication, actual availability, who receives each benefit, any financial consideration, and whether existing sponsorship commitments can meet the proposed boundary. A publicly visible code is not, by itself, proof of unauthorized disclosure.

**Recommended disclosure fields:** partner; relationship type; beneficiary; ASF receives money, goods, services, or no consideration; benefit conditions; eligible participants; any external cost; validity and availability; confirmation date; contact; approval status; conflict-of-interest review.

## 6. Finding F04: Carteirinha explanations describe different processes

**Priority: P0 — accurate membership and privacy expectations.**

The [issuance page](https://asf.surf/emitir.html) describes registration before issuance, email confirmation, no public member list, one-year initial validity, and recovery of an existing card. The [Privacy Policy](https://asf.surf/privacidade.html) describes local-only issuance and an optional central registration process. An [older operational privacy note](https://github.com/acarolmourad-commits/asf-app/blob/0373c4cb339a4d1833c83e8768bddc4e2a74eeef/docs/carteirinhas-privacy-2026-10-07.md) also describes an earlier arrangement.

The issue here is inconsistent explanation, not a tested conclusion about the underlying system.

### Clarify before promoting registration

- Is central registration required in the current public journey, or is there a genuinely separate local-only option?
- What information is necessary, what is optional, and who can access it?
- What does email confirmation establish, and how is recovery explained without promising more than the process delivers?
- Does card validity concern benefits and community access, and does it create any formal association or voting rights?
- Is issuance free, is renewal free, what happens at expiry, and how can someone obtain help?
- Which information is shown during card verification, as confirmed by the responsible owner?

Do not conflate a digital card with a government identity document, an instructional qualification, insurance, or certification of ocean readiness. Do not alter card numbers, validity, history, registration records, or consent as part of an editorial exercise.

## 7. Finding F05: member journeys need clearer expectations

| Journey | Observed strength | Main friction or disclosure gap | Recommended completion criterion |
|---|---|---|---|
| Carteirinha | Issuance and recovery explanations are available. | Registration-policy mismatch; free renewal and legal membership meaning are not sufficiently explicit. | A newcomer can explain costs, status, validity, recovery, rights, and storage before registering. |
| Diário | FAQ states that session entries remain in the browser and explains backup. | Device/browser boundaries, clearing-data risk, and switching tools need earlier explanation; progress claims sound more certain than necessary. | Before first use, the reader knows where entries are said to remain, what backup does, and that logging does not guarantee improvement. |
| Mural | Clear invitation to share and support peers. | Reviewed page/form copy does not explain public visibility, permissions for people pictured, moderation, reporting, removal, or contest conditions. | A person understands publication visibility, image permissions, support routes, and contest rules before submitting. |
| Learning guides | Free positioning, objectives, revision dates, and general safety limitations. | Uneven precision and claims; specialist language and English references need accessible context. | Each article distinguishes general information from individual advice and offers one useful next step without an implied purchase. |
| Community chat | Page explains card-based access and email confirmation. | Readers still need conduct, visibility, reporting, moderation, and emergency limitations in the participation journey. | Participation expectations are available before entering, without implying a monitored emergency service. |

Sources: [Carteirinha](https://asf.surf/emitir.html), [Recovery](https://asf.surf/recuperar-carteirinha.html), [Diário](https://acarolmourad-commits.github.io/asf-diario/), [Mural](https://asf.surf/mural/), [Mural form copy](https://github.com/acarolmourad-commits/asf-app/blob/0373c4cb339a4d1833c83e8768bddc4e2a74eeef/mural/index.html), [Learning hub](https://asf.surf/aprender/index.html), and [Community chat](https://asf.surf/sessoes-interativas.html).

## 8. Finding F06: safety-sensitive copy requires a cross-site triage

**Priority: P0 for potentially harmful instructions; P1 for overstated benefits and incentives.**

Recent guides and the [health-content review](https://github.com/acarolmourad-commits/asf-app/blob/0373c4cb339a4d1833c83e8768bddc4e2a74eeef/docs/editorial/health-content-review-2026-11-09.md) show meaningful improvements. That review explicitly limits its own scope; it is not approval of all health content across ASF.

| Triage | Copy pattern requiring attention | Editorial response |
|---|---|---|
| P0 | Attention or relaxation instructions intended for use in the water, including eyes-closed advice present in retrieved homepage text. | Hold from reuse and refer to an appropriately qualified safety reviewer; do not turn it into a do-it-yourself water exercise. |
| P0 | Breath-hold or submersion preparation instructions, or simplistic signals that imply a sea state is safe. | Check the entire content inventory, including older drafts. Do not rely on a general disclaimer to neutralize risky instructions. |
| P1 | Universal hydration, nutrition, supplement, injury-prevention, or mental-health efficacy claims. | Require an appropriate source and reviewer; distinguish a meal idea or personal experience from individualized guidance. |
| P1 | Endurance or consecutive-day rewards, such as a three-hour session or long attendance streak. | Avoid incentives that override fatigue, recovery, changing conditions, disability, work, or caring responsibilities. |
| P1 | Exact equipment prescriptions or claims of an exact volume calculation. | Explain uncertainty, suitability factors, and the role of qualified individual advice. |
| P1 | Broad rules such as earlier always being better or small waves being suitable for all beginners. | Replace universal rankings with conditional information and local assessment. |

Examples appear in [retrieved homepage copy](https://asf.surf/), the [first-board guide](https://asf.surf/aprender/primeira-prancha-de-surf.html), and [Diário educational copy](https://acarolmourad-commits.github.io/asf-diario/). Older [Instagram draft material](https://github.com/acarolmourad-commits/asf-app/blob/0373c4cb339a4d1833c83e8768bddc4e2a74eeef/instagram-content.md) also warrants review before reuse; this assessment did not establish whether those drafts were posted.

The About page's lived experience should remain a personal account, with the subject's approval. It should not be generalized into a claim that surfing treats or cures depression, panic, or another condition. Educational content and community support are not substitutes for qualified care.

## 9. Finding F07: public governance and evidence ownership are incomplete

**Priority: P1 — make accountability visible without inventing formal structures.**

The [About page](https://asf.surf/sobre.html) explains origins and past actions but does not provide a concise current governance summary. Leadership should confirm and disclose, where applicable:

- Official name and organizational status; registration details only if verified and appropriate to publish.
- Current accountable roles and how they are selected.
- How policy, expenditure, partnerships, and editorial decisions are approved.
- The difference between community participation and formal statutory membership.
- How restricted donations and conflicts of interest are handled.
- A usable complaints and safeguarding route, with a backup for reports concerning a leader.
- An appropriately aggregated account of resources and program activity.

An older [partnership proposal](https://github.com/acarolmourad-commits/asf-app/blob/0373c4cb339a4d1833c83e8768bddc4e2a74eeef/docs/proposta-parcerias.md) includes audience figures, superlatives, and guaranteed acquisition language. The stronger homepage approach avoids guaranteed reach. Leadership should require a source, measurement period, definition, owner, and permission for every public metric. Unsupported numbers should not be reused while verification is pending.

## 10. Finding F08: accessibility and localization are content responsibilities too

**Priority: P1 for essential journeys; P2 for wider consistency.**

ASF can preserve its warmth without requiring newcomers to understand every term, app name, or reward mechanic. Define manas once; explain specialist terms at first use; use descriptive link labels; distinguish saving privately from publishing; and avoid gendered assumptions about bodies, equipment, skill, or appearance.

External and satellite destinations need a short explanation of what opens, what information is carried over if anything, and how to return. Do not imply that separate tools share registration or saved data unless verified. English-language source links need a brief Portuguese explanation of their relevance. These are editorial improvements; this review does not certify keyboard, screen-reader, contrast, or device behavior.

## 11. Prioritized action plan

The roles and timings below are proposed operating assignments, not claims about existing appointments or legal deadlines.

| Order | Timing | Action | Accountable role to designate | Evidence of completion |
|---|---|---|---|---|
| 1 | First 3 days | Decide the zero-ad standard and resolve support-versus-promotion boundaries. | Authorized leadership body | Dated decision, owner, transition questions, and an approved public explanation. |
| 2 | First week | Confirm actual practices and reconcile Terms, Cookies, Privacy, mission, and funding explanations. | Leadership with privacy/legal advice as appropriate | A single approved position; unresolved questions remain explicit rather than hidden. |
| 3 | First week | Confirm membership meaning, current registration flow, validity, renewal, recovery, and privacy wording. | Membership and privacy owners | A plain-language member FAQ approved against the actual process. |
| 4 | First week | Triage high-risk health, water-safety, and incentive copy before further reuse. | Editorial lead and qualified reviewers | Review log with passage, location, decision, reviewer, source, and date. |
| 5 | Weeks 1–2 | Prepare a minimum governance and safeguarding explanation. | Leadership | Verified roles, decision routes, membership categories, reporting route, and escalation backup. |
| 6 | Weeks 1–2 | Review each current partner arrangement and evidence supporting public metrics. | Partnerships and finance owners | Confirmed relationship records; qualified benefit listings; no unsupported promises. |
| 7 | Weeks 2–3 | Clarify the four core member journeys, including Mural consent and contest information. | Member-experience and editorial coordinators | Journey checklist completed without changing application behavior by implication. |
| 8 | Within 30 days | Establish a content inventory, status labels, review cadence, and small newcomer study. | Editorial operations | Assigned owners, review dates, evidence fields, and documented usability findings. |

## 12. Validation with five newcomers

Use voluntary, informed participation. Do not require real registrations, public posts, personal health disclosures, or private member data for the study. Ask participants to explain, in their own words:

1. What is ASF, who is it for, and what is free?
2. Does ASF have advertising or subscriptions, and how does it receive support?
3. What does a Carteirinha mean, how long does it last, and where would they seek help?
4. Where does the Diário say entries remain, and what might happen when browser data is cleared?
5. Who can see a Mural post and what permissions are needed for people pictured?
6. Where can they find safety limitations, sources, and the next learning step?

Treat five participants as a diagnostic exercise, not a statistically representative survey. Record misunderstandings and completion barriers, not advertising-style conversion pressure. Report corrections completed, offers reconfirmed, content reviewed, volunteer capacity, and recurring help needs. Do not infer ocean competence from app activity.

## 13. Leadership decision register

For each item, record a decision, accountable role, date, evidence, next review, and whether public communication is authorized.

| Decision | Current status in this assessment |
|---|---|
| Definition of zero advertising and acceptable acknowledgment | Proposed charter supplied; leadership adoption pending. |
| Treatment of existing visibility-based sponsorship commitments | Requires review; no agreement was inspected or changed. |
| Formal membership and card rights | Requires confirmation against actual governance documents. |
| Current registration and privacy description | Public accounts conflict; responsible-owner confirmation required. |
| Safeguarding owner, backup, reporting route, and capacity | Appointment and operating arrangements not verified. |
| Use of audience figures, popularity claims, and guarantees | Supporting evidence and approval required before reuse. |
| Public explanation of support and use of resources | Prepare only from verified financial and program records. |

## Appendix A. Public pages read

These links document the scope of the initial review. Public pages can change after the stated review date.

1. [ASF homepage](https://asf.surf/)
2. [GitHub Pages homepage](https://acarolmourad-commits.github.io/asf-app/)
3. [About ASF](https://asf.surf/sobre.html)
4. [Partnerships](https://asf.surf/parcerias/)
5. [Surfmappers partnership](https://asf.surf/parcerias/surfmappers/)
6. [Member benefits](https://asf.surf/beneficios/)
7. [Sponsorship destination](https://patrocinio.asf.surf/)
8. [Carteirinha issuance](https://asf.surf/emitir.html)
9. [Carteirinha recovery](https://asf.surf/recuperar-carteirinha.html)
10. [Community chat](https://asf.surf/sessoes-interativas.html)
11. [Mural](https://asf.surf/mural/)
12. [Diário](https://acarolmourad-commits.github.io/asf-diario/)
13. [Learning hub](https://asf.surf/aprender/index.html)
14. [Getting started](https://asf.surf/aprender/como-comecar-a-surfar-mulheres.html)
15. [First board](https://asf.surf/aprender/primeira-prancha-de-surf.html)
16. [Surf etiquette](https://asf.surf/aprender/etiqueta-no-mar.html)
17. [Paddling](https://asf.surf/aprender/remada-tecnica-e-treinos.html)
18. [Rip-current safety](https://asf.surf/aprender/correntes-de-retorno-seguranca.html)
19. [Surf and mental well-being](https://asf.surf/bem-estar/surf-saude-mental-mulheres.html)
20. [Privacy Policy](https://asf.surf/privacidade.html)
21. [Cookie Policy](https://asf.surf/cookies.html)
22. [Terms of Use](https://asf.surf/termos-de-uso.html)

## Appendix B. Use and approval boundaries

This audit creates no policy, membership, sponsorship contract, clinical endorsement, safeguarding service, or legal conclusion. Recommendations may require separate professional advice and separately authorized work. Publication in a personal fork does not constitute ASF approval, amend its statutes, update its public policies, or change its live applications. Only the three requested Markdown documents are within this publication's scope.
