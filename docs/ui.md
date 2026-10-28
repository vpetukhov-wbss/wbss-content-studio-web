# UI implementation scope

Akveo Nebular Default light theme with Open Sans and Eva icons is the UI baseline. Use a desktop workspace with responsive navigation and a mobile campaign editor. Screens are planned; no Angular views are implemented yet.

| Screen | Main task |
| --- | --- |
| AI Studio | Enter an idea, preview context/sources, choose channels and model configuration, start generation |
| AI generation | Show Planner/Writer/Reviewer steps, partial drafts, budget/usage, cancellation and failures |
| Products and context | Manage product facts, audience, voice and evidence-backed claims |
| Sources and assets | Upload/revise supported material and inspect readiness |
| Content board | Track Idea, Draft, In review, Approved and Exported |
| Campaign editor | Edit channel variants, request an AI rewrite and compare revisions |
| AI settings and agent profile | Configure allowed providers/models, role instructions, tools and execution limits |
| Run history | Inspect saved inputs/configuration, step outcomes and usage |
| Approval and export | Review exact revisions/media and export selected formats |
| Calendar, later milestone | Schedule approved payloads and inspect delivery outcomes |

## AI experience

Start with the idea field and Generate action. Show what source revisions may be sent, which model configuration and agent workflow apply, and a bounded run limit. Missing credentials/model configuration should preserve the draft and link to settings. After starting, show the active agent, completed work, cancellation and recovery; do not hold UI progress hostage to a single long HTTP request.

The editor provides a plain-language rewrite request such as “Shorten this post and keep the demo CTA”. Show the candidate and let the user accept it into a new revision. Keep manual work and previous versions; changed payloads require new approval. Reviewer findings are advisory and include evidence references.

Provide loading, empty, error, permission-denied, cancelled and conflicting-edit states where relevant. Preserve unsaved work across tabs. Keep focus visible, controls labelled and statuses understandable without colour. Scripts and captions are separate from ready video assets. Demo fixtures must be clearly labelled and must not pretend an account is connected or content was published.
