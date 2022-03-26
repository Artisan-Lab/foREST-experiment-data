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


## Bugs found in experiment by foREST
| Project | Link | Description|
| --------- | ---------| -------- |
| GitLab-project | [detail](https://github.com/jiaxian-lin/foREST-experiment-data#forest-1) | POST /projects|
| GitLab-project | [detail](https://github.com/jiaxian-lin/foREST-experiment-data#forest-1) | POST /projects/{id}/fork/{forked_from_id}|
| GitLab-project | [detail](https://github.com/jiaxian-lin/foREST-experiment-data#forest-1)| POST /projects/{id}/share |
| GitLab-group | [detail](https://github.com/jiaxian-lin/foREST-experiment-data/edit/main/README.md#gitlab-group) | POST /groups/{id}/hooks |
| GitLab-group | [detail](https://github.com/jiaxian-lin/foREST-experiment-data/edit/main/README.md#gitlab-group) | DELETE /groups/{id} |
| GitLab-commits | [detail](https://github.com/jiaxian-lin/foREST-experiment-data/edit/main/README.md#gitlab-commits) | GET /projects/{id}/repository/commits |
| GitLab-commits | [detail](https://github.com/jiaxian-lin/foREST-experiment-data/edit/main/README.md#gitlab-commits) | POST /projects/{id}/repository/commits|
| GitLab-commits | [detail](https://github.com/jiaxian-lin/foREST-experiment-data/edit/main/README.md#gitlab-commits) | POST /projects/{id}/repository/branches|
| WordPress | [detail](https://github.com/jiaxian-lin/foREST-experiment-data/edit/main/README.md#wordpress) | DELETE /tags/{id} |
| WordPress | [detail](https://github.com/jiaxian-lin/foREST-experiment-data/edit/main/README.md#wordpress) | POST /users |
| WordPress | [detail](https://github.com/jiaxian-lin/foREST-experiment-data/edit/main/README.md#wordpress) | DELETE /categories/{id} |

## Bugs found in other APIs by foREST

this part list the Bugs we found by foREST 

| Project | Link | Status | Description |
|---------|---------|---------|---------|
| GitLab | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/334606) | submitted | POST  /hooks |
| GitLab | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/346121) | submitted | POST  /admin/clusters/add |
| GitLab | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/334610) | submitted | POST  /clusters/{id}/metrics_dashboard/annotations/ |
| GitLab | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/335276) | submitted | DELETE/PUT/GET  /users/{id}/custom_attributes/{key} |
| GitLab | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/335276) | submitted | GET  /users/{id}/custom_attributes |
| GitLab | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/334610) | submitted | POST  /projects/{id}/clusters/user |
| GitLab | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/334606) | submitted | POST  /projects/{id}/metrics/user_starred_dashboards |
| GitLab | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/335276) | submitted | DELETE/POST  /projects/{id}/custom_attributes/{key} |
| GitLab | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/334610) | submitted | POST  /projects/{id}/export | 
| GitLab | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/335276) | submitted | GET  /projects/{id}/custom_attributes |
| GitLab | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/334610) | submitted | POST  /groups/{id}/clusters/user |
| GitLab | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/335276) | submitted | GET /groups/{id}/custom_attributes |
| GitLab | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/335276) | submitted | DELETE/PUT/GET  /groups/{id}/custom_attributes/{key} |
| WordPress |  | unsubmitted | POST  /categories |
| Gitlab | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/346563) | submitted | POST projects/{id}/fork/{forked_from_id} |


## RESTler randomwalk mode experiment
<img src="https://user-images.githubusercontent.com/71680354/160048141-4fb2b6af-d44d-4ff0-b6c7-c597d41778c0.png" width = "500" height = "400" align=center />
<img src="https://user-images.githubusercontent.com/71680354/160048216-5b284ba1-e2f8-4dec-b7da-dd1c9a5db918.png" width = "500" height = "400" align=center />

