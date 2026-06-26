from selenium.webdriver.common.by import By

class StellarBurgersLocators:
    # --- Шапка сайта и Главная страница ---
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    LOGO_BUTTON = (By.XPATH, ".//div[contains(@class, 'AppHeader_header__logo')]/a")
    ACCOUNT_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")
    MAIN_LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    
    # --- Табы Конструктора бургеров ---
    TAB_BUNS = (By.XPATH, ".//span[text()='Булки']/parent::div")
    TAB_SAUCES = (By.XPATH, ".//span[text()='Соусы']/parent::div")
    TAB_FILLINGS = (By.XPATH, ".//span[text()='Начинки']/parent::div")
    ACTIVE_TAB = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current')]")

    # --- Страница Регистрации (/register) ---
    REG_NAME_INPUT = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")
    REG_EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    REG_PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    REG_SUBMIT_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    REG_INVALID_PASSWORD_ERROR = (By.XPATH, ".//p[text()='Некорректный пароль']")
    REG_LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']")

    # --- Страница Входа / Авторизации (/login) ---
    LOGIN_EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    LOGIN_PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    
    # --- Страница Восстановления Пароля (/forgot-password) ---
    FORGOT_LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']")

    # --- Страница Личного Кабинета (/account/profile) ---
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")