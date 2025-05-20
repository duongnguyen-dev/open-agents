from __future__ import annotations
from typing import List, Optional
from datetime import datetime, UTC, timedelta
from sqlalchemy import Column, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from llmbuddy.configs import SQLALCHEMY_DATABASE_URL
from llmbuddy.databases.types import ModelType, TeamArchitecture

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
)

async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

class Base(DeclarativeBase):
    pass

agentTool_table = Table(
    "agentTool_table",
    Base.metadata,
    Column("tool_id", ForeignKey("tools.id"), primary_key=True),
    Column("agent_id", ForeignKey("agents.id"), primary_key=True)
)

agentTeam_table = Table(
    "agentTeam_table",
    Base.metadata,
    Column("agent_id", ForeignKey("agents.id"), primary_key=True),
    Column("team_id", ForeignKey("teams.id"), primary_key=True)
)

class Models(Base):
    __tablename__ = "models"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    model_name: Mapped[str] = mapped_column(unique=True, index=True)
    model_type: Mapped[ModelType] = mapped_column()
    api_key: Mapped[Optional[str]] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now(UTC), onupdate=datetime.now(UTC))

    agents: Mapped[List["Agents"]] = relationship(back_populates="models")

class Tools(Base):
    __tablename__ = "tools"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    tool_name: Mapped[str] = mapped_column(unique=True, index=True)
    tool_description: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now(UTC), onupdate=datetime.now(UTC))

    agents: Mapped[List[Agents]] = relationship(secondary=agentTool_table, back_populates="tools")

class Agents(Base):
    __tablename__ = "agents"

    id: Mapped[int] = mapped_column(primary_key=True, index=True) 
    agent_name: Mapped[str] = mapped_column(unique=True, index=True)
    agent_prompt: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now(UTC), onupdate=datetime.now(UTC))

    tools: Mapped[List[Tools]] = relationship(secondary=agentTool_table, back_populates="agents")
    teams: Mapped[List[Teams]] = relationship(secondary=agentTeam_table, back_populates="agents")
    model_id: Mapped[int] = mapped_column(ForeignKey("models.id"))
    model: Mapped["Models"] = relationship(back_populates="agents")

class Teams(Base):
    __tablename__ = "teams"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    team_name: Mapped[str] = mapped_column(unique=True, index=True)
    team_architecture: Mapped[TeamArchitecture] = mapped_column()
    supervisor_prompt: Mapped[Optional[str]] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now(UTC), onupdate=datetime.now(UTC))
    
    model_id: Mapped[Optional[int]] = mapped_column(ForeignKey("models.id"))
    supervisor_model: Mapped[Optional["Models"]] = relationship(back_populates="teams")
    agents: Mapped[List[Agents]] = relationship(secondary=agentTeam_table, back_populates="teams")

class APIToken(Base):
    __tablename__ = "apitoken"

    key: Mapped[str] = mapped_column(primary_key=True, unique=True, index=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(UTC))
    expired_date: Mapped[datetime] = mapped_column(default=datetime.now(UTC) + timedelta(30))