- Code
	- class create
		- ```
		  class User(base):
		      __tablename__ = 'T_USER'	# table 이름을 의미한다
		      __table_args__ = {'extend_existing':True}
		      # extend_existing: True => 존재하면 사용하여 바꾸겠다는 의미
		  
		      pk = Column('PK', Integer, primary_key = True)
		      # 모든 attribute는 Column 객체를 생성하여 만들어줘야함
		      # 이때, Integer, Text의 경우 import하여 사용해야함
		      
		      name = Column('NAME', Text, nullable=False)
		  
		      def __repr__(self):
		          return f'pk={self.pk}, name = {self.name}'
		          # f-string으로 return하며 repr 함수가 위임되지 않도록
		          # 만들어서 return 해주게 함
		  ```
		- User를 instance화 하면 base에 저장되는 class가 된다
		- 다시말해, db와는 아무 상관이 없다
	- usage
		- ```
		  from sqlalchemy.orm import relationship, sessionmaker
		  from sqlalchemy.engine import create_engine
		  from sqlalchemy.ext.declarative import declarative_base
		  from sqlalchemy.schema import Column, ForeignKey
		  from sqlalchemy.types import Integer, Text
		  from sqlalchemy import Table
		  
		  engine = create_engine('sqlite:///:memory:', echo=True)
		  session = sessionmaker(engine)
		  sess = session()
		  base = declarative_base()
		  
		  class Artist(base):
		      __tablename__ = 'T_ARTIST'
		      __table_args__ = {'extend_existing': True}
		      pk = Column("PK", Integer, primary_key = True)
		      name = Column("NAME", Text)
		      albums = relationship('Album', back_populates='artists', uselist=True)
		  
		      def addAlbum(self, s, name):
		          a = s.query(Artist).filter(Artist.pk==self.pk).one()
		          a.albums.append(Album(name=name))
		          s.commit()
		      
		      def delAlbum(self, s, name):
		          a = s.query(Artist).filter(Artist.pk==self.pk).one()
		          a.albums.remove(list(filter(self.name==name, self.albums))[0])
		          s.commit()
		  
		      def __repr__(self):
		          return f'pk={self.pk}, name={self.name}'
		      
		  class Album(base):
		      __tablename__ = 'T_ALBUM'
		      __table_args__ = {'extend_existing': True}
		      
		      pk = Column("PK", Integer, primary_key = True)
		      name = Column("NAME", Text)
		      fk = Column("FK", None, ForeignKey(Artist.pk))
		      artist = relationship('Artist', back_populates='albums', uselist=False)
		  
		      def __repr__(self):
		          return f'pk={self.pk}, name={self.name}'
		  
		  base.metadata.create_all(engine)
		  
		  a = Artist(name='가수1')
		  sess.add(a)
		  sess.commit()
		  
		  a = sess.query(Artist).one()
		  a.addAlbum(sess, '가수1의 앨범1')
		  
		  sess.query(Album).all()
		  # 체크 확인 가능
		  
		  sess.close()
		  base.registry.dispose()
		  base.metadata.clear()
		  engine.dispose()
		  # 끝낼때 모두 초기화
		  ```