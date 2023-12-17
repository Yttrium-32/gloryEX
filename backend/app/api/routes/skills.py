from typing import List

from fastapi import APIRouter, Body, Depends, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND

from app.models.skills import CreateSkill, SkillPublic
from app.db.repositories.skills import SkillsRepository
from app.api.dependencies.database import get_repository


router = APIRouter()

@router.get("/")
async def get_all_skills() -> List[dict]:
    skills = [
        {"id": 1, "name": "John Doe", "contact_info": "john.doe@example.com", "test_data": 50},
        {"id": 2, "name": "Mary Sue", "contact_info": "mary.sue@example.com", "test_data": 100}
    ]

    return skills

@router.get("/{id}/", response_model=SkillPublic, name="skills:get-skill-by-id")
async def get_skill_by_id(
    id: int,
    skills_repo: SkillsRepository = Depends(get_repository(SkillsRepository))
    ) -> SkillPublic:
    skill = await skills_repo.get_skill_by_id(id=id)
    if not skill:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No skill found with that id.")

    return skill

@router.post("/", response_model=SkillPublic, name="skills:create-skill", status_code=HTTP_201_CREATED)
async def create_new_skill(
    new_skill: CreateSkill = Body(..., embed=True),
    skills_repo: SkillsRepository = Depends(get_repository(SkillsRepository))
    ) -> SkillPublic:
    create_skill = await skills_repo.create_skills(new_skill=new_skill)
    return create_skill


