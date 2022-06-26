hide:
    -toc

## Legend
```mermaid
flowchart TB
    {! parts/styles.md !}
    a>Initiating Event]
    b[Individual]:::member
    c[\Form/]:::form
    d[(Spreadsheet)]:::spreadsheet
```
## Data Flow
```mermaid
flowchart LR
    {! parts/styles.md !}
    {! parts/all_nodes.md !}

    subgraph new_event[New Event]
        new_fundraiser_form
        new_meeting_form
        new_mission_form
        new_sarex_form
        new_training_form
    end

    {! parts/flows/member_application_flow.md !}
    {! parts/flows/new_fundraiser_flow.md !}
    {! parts/flows/new_meeting_flow.md !}
    {! parts/flows/new_mission_flow.md !}
    {! parts/flows/new_sarex_flow.md !}
    {! parts/flows/new_training_flow.md !}
```
