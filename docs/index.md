hide:
    -toc

## Legend
```mermaid
flowchart TB
    {! styles.md !}
    a>Event]
    b[\Form/]:::form
    c[(Sheet)]:::spreadsheet
    d[Individual]:::member
```
Click on an event, form, or sheet to see all workflows associated with that item.

## Data Flow
```mermaid
flowchart LR
    {! styles.md !}
    {! all_nodes.md !}

    subgraph new_event[New Event]
        new_fundraiser_form
        new_meeting_form
        new_mission_form
        new_sarex_form
        new_training_form
    end

    {! flows/member_application_flow.md !}
    {! flows/new_fundraiser_flow.md !}
    {! flows/new_meeting_flow.md !}
    {! flows/new_mission_flow.md !}
    {! flows/new_sarex_flow.md !}
    {! flows/new_training_flow.md !}
```
