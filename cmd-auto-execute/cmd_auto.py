import subprocess
import os

def cmd_auto_execute(bashcmd):

    """ 
    # arguments

    execute shell internal -> shell=True 
    change directory -> cwd="/path"


    # execute cmd with Popen

    process = subprocess.Popen(bashcmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    output = output.decode("utf-8") # binary format -> utf-8 decoding


    # Error handling
    if(error):
        print("ERROR: " + error)
        return
    """
    
    # execute cmd with subprocess.run()
    try:
        output = subprocess.run(" ".join(bashcmd.split()), stderr=subprocess.PIPE, shell=True, cwd="C:\\Users\\CSE_125-2\\Desktop\\test")
    except output.stderr as e:
        print('Error: ' + e.decode("utf-8"))
    
    ## Print output
    print(output)


def get_filelist(path, keyword):
    # get keyword file list
    file_list = [f for f in next(os.walk(path))[2] if keyword in f]
    return file_list


if __name__ == '__main__':
    # argument
    bashcmd = "instaloader \"#cake\" --login=\"doguni96\" --password=\"dongni5566!\" -c 2 -V --fast-update"
    path = "C:\\Users\\CSE_125-2\\Desktop\\test\\#cake"
    keyword = ".jpg"

    # get file list with the ".jpg" string
    file_list = get_filelist(path, keyword)

    file_list_len = len(file_list)

    # execute command with the condition
    while file_list_len < 4:
        cmd_auto_execute(bashcmd)

        # refresh a length value of the file list
        file_list_len = len(get_filelist(path, keyword))

