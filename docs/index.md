hide:
    -toc

## Legend
```mermaid
flowchart TB
    {! styles.md !}
    a>Event]:::event
    b[\Form/]:::form
    c[(Sheet)]:::spreadsheet
    d[Individual]:::member
    e[Uncategorized]
```
Click on an event, form, or sheet to see all workflows associated with that item.

## Data Flow
```mermaid
flowchart LR
    {! styles.md !}
    {! all_flows.md !}

    subgraph new_event[New Event]
        new_fundraiser_form
        new_meeting_form
        new_mission_form
        new_sarex_form
        new_training_form
    end

    subgraph external[External Events]
        new_mission_event
        member_application_event
    end

    subgraph either[Internal or External Event]
        new_sarex_event
    end

    subgraph internal[Internal Events]
        new_training_event
        new_fundraiser_event
        new_meeting_event
    end
```
