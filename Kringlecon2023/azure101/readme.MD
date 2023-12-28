az help | less <br>
az account show <br>
az functionapp list --resource-group MyResourceGroup <br>
az vm list --resource-group northpole-rg2 <br>
az vm run-command invoke -g northpole-rg2 -n NP-VM1 --command-id RunShellScript --scripts "ls"
