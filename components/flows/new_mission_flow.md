{! events/new_mission_event.md !}

{! forms/enter_task_form.md !}
{! forms/new_mission_form.md !}
{! forms/update_dispatch_form.md !}

{! members/active_members.md !}
{! members/dispatch.md !}

{! sheets/event_log_sheet.md !}

new_mission_event --- dispatch
dispatch ---|SWANs| active_members
dispatch ---|enters| new_mission_form
new_mission_form ---|appends| event_log_sheet
new_mission_form -.-|updates| update_dispatch_form
new_mission_form -.-|updates| enter_task_form
