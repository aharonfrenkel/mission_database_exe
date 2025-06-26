import os
from typing import Optional

import mysql.connector
from dotenv import load_dotenv

from models import AgentCreate, AgentRead, AgentUpdate


load_dotenv()


class AgentDAL:
    @staticmethod
    def get_connect():
        return mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database="agents"
        )

    @classmethod
    def add_agent(cls, agent: AgentCreate) -> int:
        conn = cls.get_connect()
        cur = conn.cursor()
        sql = """
        INSERT INTO agents (code_name, real_name, location, status, missions_completed) 
        VALUES (%s, %s, %s, %s, %s)
        """
        val = (agent.code_name, agent.real_name, agent.location, agent.status, agent.missions_completed)
        cur.execute(sql, val)
        conn.commit()
        agent_id = cur.lastrowid
        cur.close()
        conn.close()
        return agent_id

    @classmethod
    def get_agent(cls, agent: AgentCreate) -> Optional[AgentRead]:
        conn = cls.get_connect()
        cur = conn.cursor()
        sql = """
        SELECT * 
        FROM agents 
        WHERE code_name = %s
        """
        val = (agent.code_name,)
        cur.execute(sql, val)
        result = cur.fetchone()
        cur.close()
        conn.close()
        return AgentRead(*result) if result else None

    @classmethod
    def update_agent(cls, agent_read: AgentRead, agent_update: AgentUpdate) -> None:
        conn = cls.get_connect()
        cur = conn.cursor()
        update_map = {k: v for k, v in agent_update.to_dict().items() if v is not None}
        sql = f"""
        UPDATE agents
        SET {', '.join([f'{k} = %s' for k in update_map.keys()])}
        WHERE id = %s
        """
        val = tuple(update_map.values()) + (agent_read.id,)
        cur.execute(sql, val)
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def delete_agent(cls, agent: AgentCreate | AgentRead) -> None:
        conn = cls.get_connect()
        cur = conn.cursor()
        sql = """
        DELETE FROM agents 
        WHERE code_name = %s
        """
        val = (agent.code_name,)
        cur.execute(sql, val)
        conn.commit()
        cur.close()
        conn.close()