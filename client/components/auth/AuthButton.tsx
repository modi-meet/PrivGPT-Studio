"use client";

import Link from "next/link";
import { Button } from "@/components/ui/button";

export function AuthButton() {
  return (
    <Button asChild>
      <Link href="/sign-in">Sign In</Link>
    </Button>
  );
}