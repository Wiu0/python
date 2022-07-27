import excel_reader as excel 
import selenium_flow as selenium
import os 

def main():
    pathFolderFiles = os.getcwd() + "/python/selenium-playground/__files" 
    sel = selenium.SeleniumReader(pathFolderFiles + "/chromedriver/chromedriver_win32/chromedriver.exe", "https://www.greenfoot.org/home")
    items = excel.read(pathFolderFiles + "/names.xlsx", 'Name')
    print("Total de itens para processar é: ", len(items), "...") 
    for item in items:
        print("processando item ", item)
        sel.initCrawler(item)
    print("Fim de execução") 
main()