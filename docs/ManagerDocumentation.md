**Регистрация**
----

* **URL**

  /api/register/2
  

* **Method:**

  `POST`
  
*  **Параметры**

   **Обязательно:**
 
   `username=[string]`
   `password=[string]`


* **Ответ**

  * **Code:** 200 <br />
    **Content:** `{ 'username' : 'string', 'password' : "hash[password]" }`
    

**Авторизация**
----

* **URL**

  /api/login/

* **Method:**

  `POST`
  
*  **Параметры**

   **Обязательно:**
 
   `username=[string]`
   `password=[string]`


* **Ответ**

  * **Code:** 200 <br />
    **Content:** `{ 'refresh' : 'string', 'access' : "string" }`
    
**Используйте ключ 'access' для авторизации**


**Добавление места**
----

* **URL**

  /api/add/place/
  
* **Method:**

  `POST`
  
*  **Параметры**

   **Обязательно:**
 
   `None`


* **Ответ**

  * **Code:** 200 <br />
    **Content:** `{ 'id' : 'int', 'description' : 'str'}`



**Изменение места**
----

* **URL**

  /api/edit/place/pk/
  
  pk - номер места
  
* **Method:**

  `PUT`
  
*  **Параметры**

   **Обязательно:**
 
   `description=[str]`


* **Ответ**

  * **Code:** 200 <br />
    **Content:** `{ 'id' : 'int', 'description' : 'str'}`

**Удаление места**
----

* **URL**

  /api/delete/place/pk/
  
  pk - номер места
  
* **Method:**

  `DELETE`
  
*  **Параметры**

   **Обязательно:**
 
   `NONE`


* **Ответ**

  * **Code:** 200 <br />
    **Content:** `None`
