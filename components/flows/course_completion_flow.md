{! events/course_completion_event.md !}
{! forms/course_completion_form.md !}
{! members/member.md !}
{! sheets/completed_courses_sheet.md !}

course_completion_event --- member
member ---|enters| course_completion_form
course_completion_form ---|appends| completed_courses_sheet
