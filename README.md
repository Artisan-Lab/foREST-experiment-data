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
| Project | Endpoint | Method | Link or description | 
|---------|---------|---------|-----------|
| GitLab | /projects | POST | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/356921) |
| GitLab | /projects/{id}/fork/{forked_from_id} | POST | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/346563) | 
| GitLab | /projects/{id}/metrics/user_starred_dashboards | POST |[issue](https://gitlab.com/gitlab-org/gitlab/-/issues/334606) |
| GitLab | /projects/{id}/clusters/user | POST | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/346121) |
| GitLab | /projects/{id}/export | POST | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/346121) |
| GitLab | /projects/{id}/custom_attributes | GET |[issue](https://gitlab.com/gitlab-org/gitlab/-/issues/335276) |
| GitLab | /projects/{id}/custom_attributes/{key} | POST | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/335276) |
| GitLab | /projects/{id}/custom_attributes/{key} | DELETE | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/335276) |
| GitLab | /projects/{id}/repository/commits | GET |[issue](https://gitlab.com/gitlab-org/gitlab/-/issues/356922) |
| GitLab | /projects/{id}/repository/commits | POST | logfile: /data/gitlab-project-branch-commit/forest/logs/5xx_request line 19 |
| GitLab | /projects/{id}/repository/branches | POST | logfile: /data/gitlab-project-branch-commit/forest/logs/5xx_request line 1897 |
| GitLab | /groups/{id}/clusters/user | POST | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/346121) |
| GitLab | /groups/{id}/custom_attributes | GET | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/335276) |
| GitLab | /groups/{id}/custom_attributes/{key} | PUT |[issue](https://gitlab.com/gitlab-org/gitlab/-/issues/335276) |
| GitLab | /groups/{id}/custom_attributes/{key} | DELETE |[issue](https://gitlab.com/gitlab-org/gitlab/-/issues/335276) |
| GitLab | /groups/{id}/custom_attributes/{key} | GET |[issue](https://gitlab.com/gitlab-org/gitlab/-/issues/335276) |
| GitLab | /users/{id}/custom_attributes | GET | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/335276) |
| GitLab | /users/{id}/custom_attributes/{key} | DELETE | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/335276) |
| GitLab | /users/{id}/custom_attributes/{key} | PUT | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/335276) |
| GitLab | /users/{id}/custom_attributes/{key} | GET | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/335276) |
| GitLab | /admin/clusters/add | POST | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/346121) |
| GitLab | /clusters/{id}/metrics_dashboard/annotations/ | POST | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/334121) |
| GitLab | /hooks | POST | [issue](https://gitlab.com/gitlab-org/gitlab/-/issues/334606) |
| WordPress| /tags/{id} | DELETE | logfile: /data/wordpress/forest/logs/5xx_request line 25 |
| WordPress| /users | POST | logfile: /data/wordpress/forest/logs/5xx_request line 41 |
| WordPress| /categories| DELETE | logfile: /data/wordpress/forest/logs/5xx_request line 17 |



## More Comparison Study with RESTler RandomWalk
<img src="https://user-images.githubusercontent.com/71680354/160048141-4fb2b6af-d44d-4ff0-b6c7-c597d41778c0.png" width = "500" height = "400" align=center />
<img src="https://user-images.githubusercontent.com/71680354/160048216-5b284ba1-e2f8-4dec-b7da-dd1c9a5db918.png" width = "500" height = "400" align=center />

