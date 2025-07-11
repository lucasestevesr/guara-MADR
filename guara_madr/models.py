from datetime import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, registry, relationship

from guara_madr.enums import GenreEnum, LanguageEnum

table_registry = registry()

@table_registry.mapped_as_dataclass
class User:
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(init= False, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)    
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), init=False)
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now(), init=False)


@table_registry.mapped_as_dataclass
class Novelist:
    __tablename__ = "novelists"

    id: Mapped[int] = mapped_column(init=False, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    
    novels: Mapped[list[Novel]] = relationship(back_populates="novelist", default_factory=list)


@table_registry.mapped_as_dataclass
class Novel:
    __tablename__ = "novels"

    id: Mapped[int] = mapped_column(init=False, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False, unique=True)
    year: Mapped[str] = mapped_column(nullable=False)
    genre: Mapped[GenreEnum] = mapped_column(nullable=True)
    language: Mapped[LanguageEnum] = mapped_column(nullable=True)
    novelist_id: Mapped[int] = mapped_column(ForeignKey("novelists.id"), nullable=False)
    novelist: Mapped[Novelist] = relationship(back_populates="novels")

