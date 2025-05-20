target = "quartus"
action = "synthesis"

syn_family="MAX 10"
syn_device = "10M08DFV817G"
syn_package = ""
syn_grade=""
syn_top = "example"
syn_project = "demo.qpf"
syn_tool = "quartus"

modules = {
    "local" : [ "../src" ],
}