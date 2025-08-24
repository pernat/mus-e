$.ajax({
    url: url_troubleshooting,
    type: "GET",
    dataType: "json",
    success: (data) => {

        const element = document.getElementById('loader');
        element.remove();


        let recentTroubleshooting = document.getElementById("troubleshooting");
        x = 0

        for (i in data.context.statuses) {
            if (x < 4) {
                let link = data.context.statuses[i]['documentation']
                toAdd = `<div class="list align-items-center border-bottom py-2">
                            <div class="wrapper w-100">
                                <p class="mb-2 font-weight-medium" id="activity_title">
                                    ${data.context.statuses[i]['description']}
                                </p>
                                <div class="d-flex justify-content-between align-items-center">
                                    <div class="d-flex align-items-center">
                                        <i class="mdi mdi-alert-outline text-muted me-1"></i>
                                        <a class="mb-0 text-small text-muted" href="${link}">Documentation</a>
                                    </div>
                                </div>
                            </div>
                        </div>`
                recentTroubleshooting.innerHTML += toAdd
                x += 1
            }
        }
        recentTroubleshooting.innerHTML += `<div class="list align-items-center pt-3">
                                  <div class="wrapper w-100">
                                    <p class="mb-0">
                                      <a href="#" class="fw-bold text-primary">Show all <i class="mdi mdi-arrow-right ms-2"></i></a>
                                    </p>
                                  </div>
                                </div>`
    },
    error: (error) => {
        console.log(error);
    }
});
