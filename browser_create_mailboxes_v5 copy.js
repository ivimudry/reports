{
    "messages": {
        "msg": [
            {
                "allowedChannels": ["SMS"],
                "from": "0000",
                "to": [
                    {
                        "number": "{{trigger.phone | remove: '+' | remove: ' ' | remove: '-' | remove: '(' | remove: ')' | remove: '_'}}"
                    }
                ],
                "minimumNumberOfMessageParts": 1,
                "maximumNumberOfMessageParts": 3,
                "body": {
                    "type": "auto",
                    "content": "{{trigger.message}}"
                },
                "reference": "cio-{{trigger.phone | remove: '+' | remove: ' ' | remove: '-' | remove: '(' | remove: ')' | remove: '_'}}-{{'now' | date: '%Y%m%d%H%M%S'}}"
            }
        ]
    }
}