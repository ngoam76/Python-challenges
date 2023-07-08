def flatten(lists_of_list):
    onedim_list = []
    for i in lists_of_list:
        onedim_list = onedim_list + i
    print(onedim_list)

flatten([[1,2],[3,4],[4,5]])