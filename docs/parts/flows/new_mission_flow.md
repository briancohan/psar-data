{! parts/nodes/events/new_mission_event.md !}

{! parts/nodes/forms/enter_task_form.md !}
{! parts/nodes/forms/new_mission_form.md !}
{! parts/nodes/forms/update_dispatch_form.md !}

{! parts/nodes/members/active_members.md !}
{! parts/nodes/members/dispatch.md !}
{! parts/nodes/members/member.md !}

{! parts/nodes/sheets/event_log_sheet.md !}
{! parts/nodes/sheets/task_log_sheet.md !}

new_mission_event --- dispatch
dispatch ---|SWANs| active_members
dispatch ---|enters| new_mission_form
new_mission_form ---|appends| event_log_sheet
new_mission_form -.-|updates| update_dispatch_form
new_mission_form -.-|updates| enter_task_form
