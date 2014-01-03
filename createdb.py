import model

model.Base.metadata.drop_all(model.engine)
model.Base.metadata.create_all(model.engine)