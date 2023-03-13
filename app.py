# Import Library
from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie


# ----- LOAD LOTTIE URL ----
def load_lottieurl(url):
    result = requests.get(url)
    if result.status_code != 200:
        return None
    return result.json()


# ----- LOAD LOCAL CSS -----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# ----- TAB TITLE -----
st.set_page_config(page_title="Library", page_icon=":book:", layout="wide")


# ----- LOAD ASSETS -----
powershell_lottie = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_c9eTLUgblo.json")
python_lottie = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_NGpl1AFNBd.json")
bash_lottie = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_tBkhDllG4M.json")
perl_lottie = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_uR3DwK9y5B.json")
vb_lottie = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_l3sfdi9x.json")
nice_work_lottie = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_L7UPXCrytj.json")
point_arrow_lottie = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_zoaqifdo.json")
local_css("style/style.css")


# ----- MAIN -----
def main():
    menu = ["PowerShell", "Python", "Bash", "Perl", "VB"]

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "PowerShell":
        # ----- HEADER SECTION -----
        with st.container():
            st.write("##")  # To Give Some Space On Top
            left_col, right_col = st.columns(2)
            with left_col:
                st.subheader("Powershell Library !!! ")
                st.write("---")  # To Create Margin Line
                st.title("Here I am sharing some of my PowerShell Codes!")
                st.write(
                    "I am passionate about finding ways to use Powershell to be more efficient and effective in "
                    "business setting")
                st.write("[Learn More About Me>](https://kaushtubh-jha.github.io/my-portfolio/)")
            with right_col:
                st_lottie(powershell_lottie, height=300, key="coding")

        # ----- SMALL DETAILS ----
        st.write("---")
        with st.container():
            left_col, middle_col, right_col = st.columns(3)
            with left_col:
                st.subheader("Enable Execution Policy")
                st.write("You might see this error if you run PowerShell first time.")
                st.error("""
                File C:\\Users\\FIle_Path\\Sample.ps1 cannot be loaded because running scripts is disabled on this 
                system. ***** UnauthorizedAccess """)
                st.info("Use this command to allow Execution Policy")
            with middle_col:
                st_lottie(point_arrow_lottie, height=300, key="arrow")
            with right_col:
                st.subheader("Command To Run")
                st.info("Set-ExecutionPolicy RemoteSigned -Scope CurrentUser")
                st.markdown("Copy this command and paste on PowerShell console and hit enter. For Pop-Up confirmation "
                            "click on **_Yes All_**. Now you are ready to use your first script. Hit run again !!!",
                            unsafe_allow_html=False)

        # ----- AUTOMATION SCRIPTS-----
        st.write("---")
        st.markdown(f'<h5 style="color:#3475eb;font-size:30px;">{"Automation Scripts"}</h5>', unsafe_allow_html=True)
        with st.container():
            col_1, col_2, col_3, col_4 = st.columns(4)

            # ----- CODE CHECKBOXES -----
            with col_1:
                PS1 = st.checkbox("GitHub Push Automatically")
            with col_2:
                PS2 = st.checkbox("Palindrome or Not")
            with col_3:
                PS3 = st.checkbox("Replace None with Recent Value")
            with col_4:
                PS4 = st.checkbox("Different Copy Command Functions")

            # ---- POWERSHELL CODES -----
            if PS1:
                st.write("You will discover how to automatically Push your all Repository into your GitHub "
                         "every day using a Windows scheduled task.")
                code = '''$Path = 'C:\\All_Repository_Folder_Path'
$Folders = Get-ChildItem -Path $Path
$Date = Get-Date
foreach ($Item in $Folders.Name)
{
    if ($Item -eq ".vscode")
    {
        continue
    }
    else
    {
        Write-Host "******* Working on $Item Repository *******" -ForegroundColor Green
        Set-Location -Path "$Path\$Item"
        git pull -q
        git add -A 
        git commit -m "$Date" -q
        git push -q
    }   
}'''
                st.code(code, language='powershell')
            if PS2:
                st.write("In this programme, will go through how to create an array, use of join and how to create/call "
                         "functions")
                code = '''# Check for Palindrome or not

Function Judge_Palindrome($arr)
{
    # Starting point is index -1 (the last character of the string) 
    # I am moving backwards towards the first character
    # Here I am just using a negative index greater than the string length -200
    $mem = $arr[-1..-200] -join '' 
    if ($arr -eq $mem) {
        return 1
    }
    return -1
}

Function Main{

    $array = 'KoloK'
    $result = Judge_Palindrome($array)
    if ($result -eq 1) {
        Write-Host "It's a Palindrome"
    }else {
        Write-Host "Not a Palindrome"
    }
}

Main
}'''
                st.code(code, language='powershell')
            if PS3:
                st.write(
                    "In this programme, will go through how to use for loop, if condition and how to create/call "
                    "functions")
                code = '''
# Given an array containing None values fill in the None values with most recent non None value in the array.
# Test case:
#     array = [1,None,2,3,None,None,5,None]
#     output = [1, 1, 2, 3, 3, 3, 5, 5]


Function None_Replace($arr)
{
    $count = 0
    foreach ($item in $arr) {
        if ($item -eq ' ') {
            $arr[$count] = $arr[$count-1]
        }
        $count++
    }
    return $arr
}

Function Main{

    $array = @(1,' ',2,3,' ',' ',5,' ')
    $replace = None_Replace($array)
    Write-Host "$replace"
}

Main'''
                st.code(code, language='powershell')
            if PS4:
                st.write(
                    "In this programme, will go through different types of Copy command examples "
                    "functions")
                code = '''#####################################################################
# Copy Item from Source to Destination can have below actions:
#####################################################################
# 1. Copy File with Copy-Item cmdlet
# 2. Recursively Copy Sub-Directories with Copy-Item cmdlet
# 3. Copy Files from Multiple Directories and Merge into One Folder
# 4. Exclude Particular File Type from Copy
# 5. Exclude a Particular File Type with Specific Name from Copy operation
# 6. Copy Files Based on Filename Prefix
# 7. Copy Files Containing Particular Keyword
# 8. Copy Files Without Preserving Directory Structure
#####################################################################


#################################
#            Examples           #
#################################

# 1. Copy File with Copy-Item cmdlet
Copy-Item C:\\Users\\Source\\Test.txt C:\\Users\\Destination

# 2. Recursively Copy Sub-Directories with Copy-Item cmdlet
Copy-Item C:\\Users\\DXZ\\Downloads\\farely\* C:\\Users\\DXZ\\Downloads\\Fare.Ly -recurse

# 3. Copy Files from Multiple Directories and Merge into One Folder
Copy-Item C:\\Users\\Source\\A\\*, C:\\Users\\Source\\B\\* C:\\Users\\Destination

# 4. Exclude Particular File Type and Folder from Copy
Copy-Item C:\\Users\\Source\\ C:\\Users\\Destination -recurse -exclude ('*.txt', 'Folder1')

# 5. Exclude a Particular File Type with Specific Name from Copy operation
Copy-Item C:\\Users\\Source\\ C:\\Users\\Destination -recurse -exclude [a-d]*.txt

# 6. Copy Files Based on Filename Prefix
Copy-Item C:\\Users\\Source C:\\Users\\Destination -filter DSC_* -recurse 

# 7. Copy Files Containing Particular Keyword
Get-ChildItem C:\\Users\\Source -recurse -filter '*DSC*.jpg' | Copy-Item -destination C:\\Users\\Destination

# 8. Copy Files Without Preserving Directory Structure
Get-ChildItem C:\\Users\\Source -recurse -force -filter "Aa*" | Copy-Item C:\\Users\\Destination'''
                st.code(code, language='powershell')
    elif choice == "Python":
        # ----- HEADER SECTION -----
        with st.container():
            st.write("##")  # To Give Some Space On Top
            left_col, right_col = st.columns(2)
            with left_col:
                st.subheader("Python Library !!! ")
                st.write("---")  # To Create Margin Line
                st.title("Here I am sharing some of my Python Codes!")
                st.write(
                    "I am passionate about finding ways to use Python to be more efficient and effective in "
                    "business setting")
                st.write("[Learn More About Me>](https://kaushtubh-jha.github.io/my-portfolio/)")
            with right_col:
                st_lottie(python_lottie, height=300, key="coding")
    elif choice == "Bash":
        # ----- HEADER SECTION -----
        with st.container():
            st.write("##")  # To Give Some Space On Top
            left_col, right_col = st.columns(2)
            with left_col:
                st.subheader("Bash Library !!! ")
                st.write("---")  # To Create Margin Line
                st.title("Here I am sharing some of my Bash Codes!")
                st.write(
                    "I am passionate about finding ways to use Bash to be more efficient and effective in "
                    "business setting")
                st.write("[Learn More About Me>](https://kaushtubh-jha.github.io/my-portfolio/)")
            with right_col:
                st_lottie(bash_lottie, height=300, key="coding")
    elif choice == "Perl":
        # ----- HEADER SECTION -----
        with st.container():
            st.write("##")  # To Give Some Space On Top
            left_col, right_col = st.columns(2)
            with left_col:
                st.subheader("Perl Library !!! ")
                st.write("---")  # To Create Margin Line
                st.title("Here I am sharing some of my Perl Codes!")
                st.write(
                    "I am passionate about finding ways to use Perl to be more efficient and effective in "
                    "business setting")
                st.write("[Learn More About Me>](https://kaushtubh-jha.github.io/my-portfolio/)")
            with right_col:
                st_lottie(perl_lottie, height=300, key="coding")
    else:
        # ----- HEADER SECTION -----
        with st.container():
            st.write("##")  # To Give Some Space On Top
            left_col, right_col = st.columns(2)
            with left_col:
                st.subheader("VB Library !!! ")
                st.write("---")  # To Create Margin Line
                st.title("Here I am sharing some of my VB Codes!")
                st.write(
                    "I am passionate about finding ways to use VB to be more efficient and effective in "
                    "business setting")
                st.write("[Learn More About Me>](https://kaushtubh-jha.github.io/my-portfolio/)")
            with right_col:
                st_lottie(vb_lottie, height=300, key="coding")

    # ----- CONTACT FORM -----
    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("Feel free to share the suggestions and correction regarding codes. I will try my best to apply your"
                 "ideas. If there is something you want me to put here, I will be happy to help and provide you "
                 "the code here or as well as in GitHub for community share.")
        st.write("##")

        contact_form = """
        <form action="https://formsubmit.co/kaushtubhjha45.kj@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder= "Your name" required>
            <input type="email" name="email" placeholder= "Your email" required>
            <textarea name="message" name="email" placeholder= "Your message here..." required></textarea>
            <button type="submit">Send</button>
        </form>
        """

        left_col, right_col = st.columns(2)
        with left_col:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_col:
            st.empty()


if __name__ == "__main__":
    main()
