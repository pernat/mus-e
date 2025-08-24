$.ajax({
    url: url_projects,
    type: "GET",
    dataType: "json",
    success: (data) => {
        let jiraProjectsDashboard = document.getElementById("jira-projects-dashboard");
        jiraProjectsDashboard.innerHTML = data.context.length

    },
    error: (error) => {
        console.log(error);
    }
});
