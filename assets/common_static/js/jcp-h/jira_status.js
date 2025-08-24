$.ajax({
    url: url_status,
    type: "GET",
    dataType: "json",
    success: (data) => {
        let jiraStatusDashboard = document.getElementById("jira-status-dashboard");
        jiraStatusDashboard.innerHTML = data.context.state

    },
    error: (error) => {
        console.log(error);
    }
});
