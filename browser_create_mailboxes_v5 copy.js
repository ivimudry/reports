{
   "messages": {
       "msg": [                          // масив повідомлень (можна кілька, але ми шлемо 1)
           {
               "allowedChannels": ["SMS"],    // канал доставки — тільки SMS
               "from": "PantherBet",          // ім'я відправника (що побачить отримувач)
               "to": [                        // кому відправити
                   {
                       "number": "{{trigger.phone | remove: '+'}}"  
                       // номер телефону з тригера, з видаленням "+" якщо є
                   }
               ],
               "minimumNumberOfMessageParts": 1,   // мінімум 1 частина SMS
               "maximumNumberOfMessageParts": 3,   // максимум 3 частини (якщо текст довгий)
               "body": {
                   "type": "auto",            // автоматичне визначення кодування (GSM або Unicode)
                   "content": "{{trigger.message}}"  // текст SMS з тригера
               },
               "reference": "cio-{{trigger.phone}}"  // унікальний ID для трекінгу в CM.com
           }
       ]
   }
}