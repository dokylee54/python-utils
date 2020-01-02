'''
    move file
'''
# moving a file to different directory

def move_file(filename, src_dir, des_dir):
    import shutil

    shutil.move(src_dir + filename, des_dir + filename)


'''
    example
'''
if __name__ == "__main__":
    
    filename = "test.jpeg"

    src_dir = "test_folder/test_img/test_img_before/"
    des_dir = "test_folder/test_img/test_img_after/"

    move_file(filename, src_dir, des_dir)
