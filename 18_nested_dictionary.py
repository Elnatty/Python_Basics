try:
    nested_dict = {'a': True,
                   'b': [{u'message':{u'chat':{u'first_name':u'Jackson',
                                             u'id':94706906,
                                             u'last_name':u'Victor',
                                             u'type':u'private'},
                                     u'date': 452879205,
                                     u'entities': [{u'length': 6,
                                                    u'offset': 0,
                                                    u'type': u'bot_command'}],
                                     }},
                         {u'update_id': 365456275}]
                   }
    for items in nested_dict['b']:
        print(items['message']['chat'])
except KeyError:
    print('')