{
    "messages": {
        "msg": [
            {
                "allowedChannels": ["SMS"],
                "from": "PantherBet",
                "to": [
                    {
                        "number": "{{trigger.phone | remove: '+' | remove: ' ' | remove: '-' | remove: '(' | remove: ')' | remove: '_' | prepend: '00'}}"
                    }
                ],
                "minimumNumberOfMessageParts": 1,
                "maximumNumberOfMessageParts": 3,
                "body": {
                    "type": "auto",
                    "content": "{{trigger.message}}"
                },
                "reference": "cio-{{trigger.phone | remove: '+' | remove: ' ' | remove: '-' | remove: '(' | remove: ')' | remove: '_' | prepend: '00'}}-{{'now' | date: '%Y%m%d%H%M%S'}}"
            }
        ]
    }
}