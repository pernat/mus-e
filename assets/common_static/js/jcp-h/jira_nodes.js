$.ajax({
    url: url_cluster,
    type: "GET",
    dataType: "json",
    success: (data) => {
        console.log('Good')
        let jiraNodesDashboard = document.getElementById("jira-nodes-dashboard");
        if (data.context.errorMessages[0].includes("This Jira instance is not clustered.")) {
            jiraNodesDashboard.innerHTML = "1"
        } else {
            jiraNodesDashboard.innerHTML = "?"
        }


    },
    error: (error) => {
        console.log('Error')
        let jiraNodesDashboard = document.getElementById("jira-nodes-dashboard");
        jiraNodesDashboard.innerHTML = "No data"
    }
});
