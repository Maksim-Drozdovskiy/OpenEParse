from utils import authorizer, fix_bads, get_problem, save_to_excel

USERNAME = "MaksimDrozdovskiy"
PASSWORD = "Mak$1M.O0mm5k!!y"
COURSE_URL = "https://apps.openedu.ru/learning/course/course-v1:ITMOUniversity+DIGCUL+fall_2023_urfu/home"

if __name__ == "__main__":
    print("Connecting...")
    client = authorizer(USERNAME, PASSWORD)
    page = fix_bads(client.get(COURSE_URL).text)
    save_to_excel(get_problem(page), 'out.xlsx')
    print("Finish!")
