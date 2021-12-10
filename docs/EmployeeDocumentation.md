**Регистрация**
----

* **URL**

  /api/register/1
  

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


**Просмотр всех мест**
----

* **URL**

  /api/places/
  

* **Method:**

  `GET`
  
*  **Параметры**

   **Обязательно:**
 
   `NONE`
 

* **Ответ**

  * **Code:** 200 <br />
    **Content:** `{ 'id' : 'int', 'description' : "str" }`
    
    
**Просмотр занятого времени конкретного места**
----

* **URL**

  /api/places/pk/
  
  pk - номер места

* **Method:**

  `GET`
  
*  **Параметры**

   **Обязательно:**
 
   `NONE`


* **Ответ**

  * **Code:** 200 <br />
    **Content:** `cписок занятого времени конкретного места`
 
**Добавление брони конкретного места**
----

* **URL**

  /api/add/time/
  
* **Method:**

  `POST`
  
*  **Параметры**

   **Обязательно:**
 
   `time=[int] - конкретный час этого дня`
   `duration=[int] - продолжительность бронирования`
   `parking_place_id=[int] - идентификатор места`


* **Ответ**

  * **Code:** 200 <br />
    **Content:** `{ 'time' : 'int', 'duration' : 'int' , 'parking_place_id' : 'int'}`

**Просмотр своих броней**
----

* **URL**

  /api/get/time/
  
  pk - номер места

* **Method:**

  `GET`
  
*  **Параметры**

   **Обязательно:**
 
   `NONE`


* **Ответ**

  * **Code:** 200 <br />
    **Content:** `cписок броней конкретного пользователя`
    
**Удаление брони**
----

* **URL**

  /api/delete/time/pk/
  
  pk - номер брони

* **Method:**

  `DELETE`
  
*  **Параметры**

   **Обязательно:**
 
   `NONE`


* **Ответ**

  * **Code:** 200 <br />
    **Content:** `None`

 
   
 
