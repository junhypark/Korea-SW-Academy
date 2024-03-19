- JSON이란 data를 text 형태로 저장할 수 있도록 만들어주는 타입이다
- 안의 값들은 dictionary로 되어 있으며 dict안의 값들은 list로 넣을 수 있다
- ex)
- ```
  {
      "glossary": {
          "title": "example glossary",
  		"GlossDiv": {
              "title": "S",
  			"GlossList": {
                  "GlossEntry": {
                      "ID": "SGML",
  					"SortAs": "SGML",
  					"GlossTerm": "Standard Generalized Markup Language",
  					"Acronym": "SGML",
  					"Abbrev": "ISO 8879:1986",
  					"GlossDef": {
                          "para": "A meta-markup language, used to create markup languages such as DocBook.",
  						"GlossSeeAlso": ["GML", "XML"]
                      },
  					"GlossSee": "markup"
                  }
              }
          }
      }
  }
  ```