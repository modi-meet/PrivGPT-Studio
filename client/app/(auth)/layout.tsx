import React from "react";
import Header from "@/components/ui/header";
import Footer from "@/components/ui/footer";

export default function AuthLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <>
      <Header />
      <main className="flex items-center justify-center w-full py-2">
        {children}
      </main>
      <Footer />
    </>
  );
}