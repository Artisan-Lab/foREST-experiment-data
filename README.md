# foREST

This is the repo for the paper **foREST: A Tree-based Approach for Fuzzing RESTful APIs** submitted to ISSTA 2022.

The repository contains two folders:
1. `source code`: source code of foREST
2. `experiment data`: the coverage growth recorded during our experiment, the full logs are available here: 


## Instructions to Run foREST 

Step 1. Clone the repo and install the dependencies
```bash
pip3 install -r requirements.txt
```

Step 2. Save the yaml doc of the target service to the folder of `openapi`

Step 3. Configue to use the yamal file via [FoREST_config](https://github.com/jiaxian-lin/foREST-experiment-data/blob/main/code/foREST/FoREST_config.conf).

Step 4. run
```bash
python3 main.py
```

## All Bugs Found by foREST

| Project | Link | Description |
|---------|---------|---------|---------|
| GitLab | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/334606) | POST  /hooks |
| GitLab | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/346121) | POST  /admin/clusters/add |
| GitLab | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/334610) | POST  /clusters/{id}/metrics_dashboard/annotations/ |
| GitLab | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/335276) | DELETE/PUT/GET  /users/{id}/custom_attributes/{key} |
| GitLab | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/335276) | GET  /users/{id}/custom_attributes |
| GitLab | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/334610) | POST  /projects/{id}/clusters/user |
| GitLab | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/334606) | POST  /projects/{id}/metrics/user_starred_dashboards |
| GitLab | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/335276) | DELETE/POST  /projects/{id}/custom_attributes/{key} |
| GitLab | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/334610) | POST  /projects/{id}/export | 
| GitLab | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/335276) | GET  /projects/{id}/custom_attributes |
| GitLab | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/334610) | POST  /groups/{id}/clusters/user |
| GitLab | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/335276) | GET /groups/{id}/custom_attributes |
| GitLab | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/335276) | DELETE/PUT/GET  /groups/{id}/custom_attributes/{key} |
| WordPress |  |  POST  /categories |
| Gitlab | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/346563) | POST projects/{id}/fork/{forked_from_id} |


## More comparison experiments with RESTler randomwalk
<img src="https://user-images.githubusercontent.com/71680354/160048141-4fb2b6af-d44d-4ff0-b6c7-c597d41778c0.png" width = "500" height = "400" align=center />
<img src="https://user-images.githubusercontent.com/71680354/160048216-5b284ba1-e2f8-4dec-b7da-dd1c9a5db918.png" width = "500" height = "400" align=center />

