$.ajax({
    url: url_serverinfo,
    type: "GET",
    dataType: "json",
    success: (data) => {
        let jiraServerinfoDashboard = document.getElementById("jira-status-serverinfo");
        jiraServerinfoDashboard.innerHTML = data.context.version

    },
    error: (error) => {
        console.log(error);
    }
});
