{
   "messages": {
       "msg": [                          // масив повідомлень (можна кілька, але ми шлемо 1)
           {
               "allowedChannels": ["SMS"],    // канал доставки — тільки SMS
               "from": "PantherBet",          // ім'я відправника (що побачить отримувач)
               "to": [                        // кому відправити
                   {
                       "number": "{{trigger.phone | remove: '+'}}"  
                       // номер телефону з тригера, з видаленням "+" якщо є, щоб формат відповідав вимогам CM.com
                   }
               ],
               "minimumNumberOfMessageParts": 1,   // мінімум 1 частина SMS (153 символів для GSM (латиниця, цифри) або 67 для Unicode (кирилиця, емодзі))
               "maximumNumberOfMessageParts": 3,   // максимум 3 частини (459 символів для GSM (латиниця, цифри) або 201 для Unicode (кирилиця, емодзі))
               "body": {
                   "type": "auto",            // автоматичне визначення кодування (GSM або Unicode)
                   "content": "{{trigger.message}}"  // текст SMS з тригера (те що надсилає CM.com)
               },
               "reference": "cio-{{trigger.phone}}"  // унікальний ID для трекінгу в CM.com
           }
       ]
   }
}