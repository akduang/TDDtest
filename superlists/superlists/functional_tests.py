from selenium import webdriver # type: ignore
brower = webdriver.Firefox()

brower.get('http://localhost:8000')
# print(brower.title)
# assert 'django' in brower.title
assert 'The install worked successfully! Congratulations!' in brower.title