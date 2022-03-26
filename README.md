# foREST

This is the repo for the paper **foREST: A Tree-based Approach for Fuzzing RESTful APIs** submitted to ISSTA 2022.

The repository contains two folders:
1. `source code`: source code of foREST
2. `experiment data`: the coverage growth recorded during our experiment, the full logs are available [here](https://drive.google.com/file/d/1rKKNu1W7lXijf2rAenmtnE2JeoTyfYxk/view?usp=sharing) 


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
| Project | Endpoint | Link or description | 
|---------|---------|---------|
| GitLab | POST projects/{id}/fork/{forked_from_id} | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/346563) | 
| GitLab | POST projects | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/356921) |
| GitLab | GET /projects/{id}/repository/commits | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/356922) |
| GitLab | POST  /admin/clusters/add | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/346121) |
| GitLab | POST  /projects/{id}/clusters/user | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/346121) |
| GitLab | POST  /projects/{id}/export |  [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/346121) |
| GitLab | POST  /groups/{id}/clusters/user | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/346121) |
| GitLab | POST  /clusters/{id}/metrics_dashboard/annotations/ | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/334121) |
| GitLab | DELETE/PUT/GET  /users/{id}/custom_attributes/{key} | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/335276) |
| GitLab | DELETE/POST  /projects/{id}/custom_attributes/{key} | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/335276) |
| GitLab | GET  /projects/{id}/custom_attributes | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/335276) |
| GitLab | GET  /users/{id}/custom_attributes | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/335276) |
| GitLab | GET /groups/{id}/custom_attributes | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/335276) |
| GitLab | DELETE/PUT/GET  /groups/{id}/custom_attributes/{key} | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/335276) |
| GitLab | POST  /hooks | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/334606) |
| GitLab | POST  /projects/{id}/metrics/user_starred_dashboards | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/334606) |
| WordPress| DELETE /tags/{id} | not support |
| WordPress| POST /users | create an existing user |
| WordPress| DELETE /categories| not support |



## More Comparison Study with RESTler RandomWalk
<img src="https://user-images.githubusercontent.com/71680354/160048141-4fb2b6af-d44d-4ff0-b6c7-c597d41778c0.png" width = "500" height = "400" align=center />
<img src="https://user-images.githubusercontent.com/71680354/160048216-5b284ba1-e2f8-4dec-b7da-dd1c9a5db918.png" width = "500" height = "400" align=center />

