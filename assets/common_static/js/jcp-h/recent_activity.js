$.ajax({
    url: url_activity,
    type: "GET",
    dataType: "json",
    success: (data) => {
        let recentActivity = document.getElementById("events");
        for (i in data.context.records.reverse()) {
            toAdd = `<div class="list align-items-center border-bottom py-2">
                        <div class="wrapper w-100">
                            <p class="mb-2 font-weight-medium" id="activity_title">
                                ${data.context.records[i]['summary']} - ${data.context.records[i]['objectItem']['name']}
                            </p>
                            <div class="d-flex justify-content-between align-items-center">
                                <div class="d-flex align-items-center">
                                    <i class="mdi mdi-calendar text-muted me-1"></i>
                                    <p class="mb-0 text-small text-muted">${data.context.records[i]['created']}</p>
                                </div>
                            </div>
                        </div>
                    </div>`
            recentActivity.innerHTML += toAdd

        }
    },
    error: (error) => {
        console.log(error);
    }
});
